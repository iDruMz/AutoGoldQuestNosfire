from phoenixapi import phoenix
from time import sleep
import json

def initialize_apis(ports):
    return [phoenix.Api(port) for port in ports]

def start_action_and_sell(api_instances, delay=0.05):
    for api in api_instances:
        packet_buy = "buy 2 2740 8 999"
        api.send_packet(packet_buy)
        print("Buy action started")

        sleep(delay)  # Petit délai de 50 ms avant la vente

        packet_sell = "sell 2 2740 2 0 999 0"
        api.send_packet(packet_sell)
        print("Sell action started")

        global money_spent
        money_spent += 999
        print(f"Money: {money_spent}/25kk")

if __name__ == "__main__":
    print("Port phoenix bot :")
    port = input("Entrez le port PhoenixAPI à utiliser : ")
    ports = [int(port)]
    api_instances = initialize_apis(ports)
    
    global money_spent
    money_spent = 0
    
    while True:
        start_action_and_sell(api_instances)
        sleep(0.5)  # Délai entre chaque boucle

    # Note: La boucle while True continuera indéfiniment jusqu'à ce que le programme soit arrêté manuellement
