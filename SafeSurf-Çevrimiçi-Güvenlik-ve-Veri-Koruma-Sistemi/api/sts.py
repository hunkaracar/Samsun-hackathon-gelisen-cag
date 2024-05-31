import subprocess
import pandas as pd
import socket
import sys
import numpy as np
import joblib
import tempfile

def text(url):
    print(url)
    predict(url)

def predict(text):
    domain = text
    ip_address = resolve_domain_ip(domain)
    tshark_command = prepare_tshark_command(ip_address)

    temp_filename = run_tshark_command(tshark_command)

    df = read_temp_file(temp_filename)

    fill_missing_values(df)

    model = load_model('model.pkl')

    predictions = predict_with_model(df, model)


    print_predictions(predictions)

    delete_temp_file(temp_filename)

def resolve_domain_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Çözülen IP adresi: {ip_address}")
        return ip_address
    except socket.gaierror:
        print(f"Hata: {domain} alan adı çözümlenemedi.")
        sys.exit(1)

def prepare_tshark_command(ip_address):
    return [
        "tshark", 
        "-i", "eth0", 
        "-a", "duration:20",  # 20 saniye süreyle dinle
        "-T", "fields",
        "-E", "header=y",
        "-E", "separator=,",
        "-E", "quote=d", 
        "-E", "occurrence=f",
        "-e", "icmp.type",
        "-e", "tcp.flags.fin",
        "-e", "frame.time_delta",
        "-e", "tcp.flags.syn",
        "-e", "tcp.flags.push",
        "-e", "udp.srcport",
        "-e", "ssh",
        "-e", "frame.number",
        "-e", "frame.time_delta_displayed",
        "-e", "ip.proto",
        "-e", "http",
        "-e", "frame.len",
        "-e", "tcp.hdr_len",
        "-e", "tcp.flags.syn",
        "-e", "tcp.flags.ack",
        "-e", "tcp.flags.urg",
        "-e", "frame.time_relative",
        "-e", "frame.time_delta_displayed",
        "-e", "tcp.flags.urg",
        "-e", "tcp.flags.ack",
        "-e", "tcp.flags.reset",
        "-e", "tcp.flags.push",
        "-e", "tcp.flags.syn",
        "-e", "tcp.flags.fin",
        "-e", "tcp.flags.syn",
        f"host {ip_address}"
    ]

def run_tshark_command(command):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_file:
        temp_filename = temp_file.name
        process = subprocess.Popen(command, stdout=temp_file)

        try:
            process.wait()
        except KeyboardInterrupt:
            process.kill()

    return temp_filename

def read_temp_file(filename):
    df = pd.read_csv(filename)
    print("Orijinal DataFrame:")
    print(df.head(5))
    return df

def fill_missing_values(df):
    for col in df.columns:
        for i in range(len(df[col])):
            if pd.isnull(df.at[i, col]):
                df.at[i, col] = 0.0
    print("Eksik değerleri doldurulmuş DataFrame:")
    print(df.head(5))

def load_model(model_filename):
    return joblib.load(model_filename)

def predict_with_model(df, model):
    predictions = []
    for index, row in df.iterrows():
        values = row.values
        y_pred = model.predict([values])
        predictions.append(y_pred)
    return predictions

def print_predictions(predictions):
    print("Tahmin edilen değerler:")
    print(predictions)
    unique_predictions = np.unique(predictions)
    for prediction in unique_predictions:
        print(f"Saldırı Türü: {prediction}")

def delete_temp_file(filename):
    import os
    os.remove(filename)