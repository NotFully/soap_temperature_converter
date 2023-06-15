from zeep import Client

client = Client('http://localhost:8000/soap/converter/?wsdl')

response = client.service.celsius_to_fahrenheit(celsius=float(input('Введите температуру в целсиях: ')))
result = response

print(f"Результат перевода: {result} градусов Фаренгейта")
