from django.views.decorators.csrf import csrf_exempt
from spyne import Application, rpc, ServiceBase, Float
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication


class TemperatureConverterService(ServiceBase):
    @rpc(Float, _returns=Float)
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32


temperature_converter_soap_service = csrf_exempt(DjangoApplication(
    Application([TemperatureConverterService],
    'converter',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11())
))
