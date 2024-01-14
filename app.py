import streamlit as st
import requests
import json
import locale


def get_prediction(data):

    print(json.dumps(data))

    endpoint = st.secrets["API-ENDPOINT"]
    headers = {'x-api-key': st.secrets["API-KEY"], 'Content-Type': 'application/json'}

    response = requests.post(endpoint, data=json.dumps(data), headers=headers)
    
    if response.status_code == 200:
        result = (response.json())
        print(result)

        """
        ### Preço estimado para compra

        De acordo com os dados fornecidos, seu laptop poderá ser comprado pelo seguinte valor abaixo.
        """

        locale.setlocale(locale.LC_ALL, 'pt_BR')
        predicted_value_formatted = locale.format_string("%d", result['prediction'], grouping=True)


        st.markdown("Modelo consultado com sucesso.")
        st.markdown("Valor para compra: **" + str(predicted_value_formatted) + " IND (India Rupee)**.")
    else:
        st.markdown("Houve um problema na consulta. Revise os dados.")

"""
# Machine Learning Engineering

## Predição de Preço de Laptop

Este modelo é capaz de prever o preço de um laptop dada algumas características.

A aplicação é para ser utilizada em uma loja eletrônica que avalia laptops usados como parte do pagamento de um novo, 
por tal razão a avaliação não é tão exaustiva e se baseia em caracteríticas comuns, como marca, processador, memória etc.
sem nenhuma outra avaliação visual, pelo menos por enquanto.

### Características do laptop
"""


brand_option = st.selectbox(
    "Qual é a marca?",
    ("Asus", "Dell", "HP", "Lenovo", "Outro"))

touchscreen = st.radio(
    "Possui touchscreen (tela sensível ao toque)?",
    ["Não", "Sim"])

processor_brand = st.radio(
    "Qual a marca do processor?",
    ["AMD", "Intel", "M1"])

brand_option = st.selectbox(
    "Qual é o nome do processador?",
    ("Core i3", "Core i5 ", "Core i7", "Ryzen 5", "Ryzen 7", "Outro"),)

os_bit = st.radio(
    "Qual a arquitetura do sistema operacional?",
    ["32 bits", "64 bits"])

os_brand = st.radio(
    "Qual o sistema operacional?",
    ["Windows", "Outro"])

weight = st.radio(
    "Qual o peso estimado?",
    ["Casual", "Gaming", "Thinlight"],
    captions = ["Peso padrão", "Pesado", "Leve"])

warranty = st.radio(
    "Qual a garantia atual?",
    ["Sem garantia", "1 ano", "2 anos", "3 anos"])

ram_type = st.radio(
    "Qual o tipo da memória RAM?",
    ["DDR4", "Outro"])

ram_size = st.selectbox(
    "Qual é o tamanho da memória RAM?",
    ("4 GB", "8 GB", "16 GB", "32 GB",))

hdd_size = st.selectbox(
    "Qual é o tamanho do armazenamento em disco estado sólido (SSD)?",
    ("Sem HDD (apenas SSD)", "512 GB", "1 TB", "2 TB"))

ssd_size = st.selectbox(
    "Qual é o tamanho do armazenamento em disco rígido (HDD)?",
    ("Sem SSD (apenas HDD)", "128 GB", "256 GB", "512 GB", "1 TB", "2 TB", "3 TB"))


graphic_card_option = st.selectbox(
    "Qual é o tamanho da memória gráfica (vídeo)?",
    ("4 GB", "8 GB", "16 GB", "32 GB"))

if brand_option == "Outro":
    brand_option = "other"

if os_brand == "Outro":
    os_brand = "other"

if warranty == "Sem garantia":
    warranty = "0"
else:
    warranty = warranty.replace(" ano", "")
    warranty = warranty.replace(" anos", "")

os_bit = os_bit.replace(" bits", "")

if ram_type == "Outro":
    ram_type = "other"

ram_size = ram_size.replace(" GB", "")

hdd_size = hdd_size.replace("Sem HDD (apenas SSD)", "0")
hdd_size = hdd_size.replace(" GB", "")
hdd_size = hdd_size.replace(" TB", "")

ssd_size = hdd_size.replace("Sem SSD (apenas HDD)", "0")
ssd_size = ssd_size.replace(" GB", "")
ssd_size = ssd_size.replace(" TB", "")


if touchscreen=="Sim":
    touchscreen = "1"
else:
    touchscreen = "0"

graphic_card_option = graphic_card_option.replace(" GB", "")

payload = { "data" : {
        "brand": brand_option.lower(),
        "processor_brand": processor_brand.lower(),
        "processor_name": brand_option.lower(),
        "os": os_brand.lower(),
        "weight": weight.lower(),
        "warranty": warranty,
        "touchscreen": touchscreen,
        "ram_gb": ram_size,
        "hdd": hdd_size,
        "ssd": ssd_size,
        "graphic_card": graphic_card_option,
        "ram_type": ram_type.lower(),
        "os_bit": os_bit
    }
}


if st.button("Estimar Preço"):
    with st.spinner("Processando..."):
        get_prediction(payload)

