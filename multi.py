import time
import threading

def fazer_requisicao_web():
    print("Fazendo requisição web...")
    time.sleep(3)
    print("Terminei a requisição")


thread_1 = threading.Thread(target=fazer_requisicao_web)
thread_1.start()

thread_2 = threading.Thread(target=fazer_requisicao_web)
thread_2.start()

thread_3 = threading.Thread(target=fazer_requisicao_web)
thread_3.start()