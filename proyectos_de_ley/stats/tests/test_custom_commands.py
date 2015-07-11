from django.test import TestCase
from django.core.management import call_command

from pdl.models import Proyecto
from pdl.models import Seguimientos
from stats.models import ComisionCount
from stats.models import Dispensed


class TestCustomCommand(TestCase):
    def setUp(self):
        b = Proyecto(**{
            'codigo': '00586',
            'numero_proyecto': '00586/2011-CR',
            'fecha_presentacion': '2010-10-10',
            'short_url': '4huj5x',
            'iniciativas_agrupadas': '{00001,00002,00586}',
            'titulo_de_ley': 'Titulo de Ley',
            'id': 1,
        })
        b1 = Proyecto(**{
            'codigo': '00001',
            'numero_proyecto': '00001/2011-CR',
            'fecha_presentacion': '2010-10-10',
            'short_url': '4auj5a',
            'id': 2,
        })
        c = Seguimientos(**{
            'fecha': '2012-10-10',
            'evento': 'en comisión Justicia',
            'proyecto': b,
        })
        c1 = Seguimientos(**{
            'fecha': '2012-10-10',
            'evento': 'Dispensado 2da Votación',
            'proyecto': b,
        })
        c2 = Seguimientos(**{
            'fecha': '2012-10-10',
            'evento': 'Promulgado Ley No: 29971',
            'proyecto': b,
        })
        c3 = Seguimientos(**{
            'fecha': '2012-10-10',
            'evento': 'Publicado: Ley No: 29971',
            'proyecto': b,
        })
        b.save()
        b1.save()
        c.save()
        c1.save()
        c2.save()
        c3.save()
        call_command('create_stats')

    def test_create_stats(self):
        res = ComisionCount.objects.all()
        expected = 1
        for i in res:
            self.assertEqual(expected, i.count)

    def test_all_iniciativas_with_title_of_law(self):
        res = Proyecto.objects.get(codigo='00001')
        expected = 'Titulo de Ley'
        result = res.titulo_de_ley
        self.assertEqual(expected, result)

    def test_get_dispensados_2da_votacion(self):
        res = Dispensed.objects.all()
        expected = 1
        self.assertEqual(expected, res[0].total_dispensed)

    def test_get_aprobados(self):
        res = Dispensed.objects.all()
        expected = 1
        self.assertEqual(expected, res[0].total_approved)
