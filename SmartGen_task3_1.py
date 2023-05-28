import requests
import time
from datetime import datetime
import matplotlib.pyplot as plt

class StorageProviderMonitor:
    def __init__(self, provider_ids):
        self.provider_ids = provider_ids
        self.timestamps = []
        self.capacity_values = []
        self.bandwidth_usage_values = []
        self.latency_values = []
        self.uptime_values = []
    
    def get_storage_provider_stats(self, provider_id):
        url = f"https://api.bnb.greenfield/providers/{provider_id}/stats"
        response = requests.get(url)
        if response.status_code == 200:
            stats = response.json()
            return stats
        else:
            return None
    
    def process_stats(self, stats):
        capacity = stats["capacity"]
        bandwidth_usage = stats["bandwidth_usage"]
        latency = stats["latency"]
        uptime = stats["uptime"]
        
        # Обработка и анализ показателей
        # ...
        
        if capacity > threshold:
            self.send_alert(f"Превышена емкость хранилища: {capacity}")
        if bandwidth_usage > threshold:
            self.send_alert(f"Превышено использование полосы пропускания: {bandwidth_usage}")
        if latency > threshold:
            self.send_alert(f"Превышена задержка: {latency}")
        if uptime < threshold:
            self.send_alert(f"Низкое время безотказной работы: {uptime}")
        
        # Добавление значений в список для визуализации
        self.timestamps.append(datetime.now())
        self.capacity_values.append(capacity)
        self.bandwidth_usage_values.append(bandwidth_usage)
        self.latency_values.append(latency)
        self.uptime_values.append(uptime)
    
    def send_alert(self, alert_message):
        # Отправка уведомления или оповещения, например, по электронной почте или через мессенджер
        # ...
    
    def monitor_storage_providers(self):
        while True:
            for provider_id in self.provider_ids:
                stats = self.get_storage_provider_stats(provider_id)
                if stats:
                    self.process_stats(stats)
            
            self.plot_performance()
            
            time.sleep(interval_seconds)  # Интервал между проверками
    
    def plot_performance(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.timestamps, self.capacity_values, label='Capacity')
        plt.plot(self.timestamps, self.bandwidth_usage_values, label='Bandwidth Usage')
        plt.plot(self.timestamps, self.latency_values, label='Latency')
        plt.plot(self.timestamps, self.uptime_values, label='Uptime')
        plt.xlabel('Time')
        plt.ylabel('Performance')
        plt.title('Storage Provider Performance')
        plt.legend()
        plt.show()

# Конфигурация и запуск монитора
provider_ids = [...]  # список идентификаторов провайдеров хранения данных
interval_seconds = 60  # интервал между проверками в секундах
threshold = ...  # пороговые значения для определения проблем

monitor = StorageProviderMonitor(provider_ids)
monitor.monitor_storage_providers()
