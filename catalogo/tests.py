from django.test import TestCase
from catalogo.models import Terrenos


class TerrenosModelTest(TestCase):
    def test_create_terreno(self):
        terreno = Terrenos.objects.create(
            frente=10.50,
            fondo=20.30,
            precio=150000.00,
            name="Test Terreno",
            imagen="https://example.com/img.jpg",
        )
        self.assertEqual(terreno.frente, 10.50)
        self.assertEqual(terreno.fondo, 20.30)
        self.assertEqual(terreno.precio, 150000.00)
        self.assertEqual(terreno.name, "Test Terreno")
        self.assertEqual(terreno.imagen, "https://example.com/img.jpg")

    def test_string_representation(self):
        terreno = Terrenos.objects.create(
            frente=10.50,
            fondo=20.30,
            precio=150000.00,
            name="Test Terreno",
            imagen="https://example.com/img.jpg",
        )
        self.assertEqual(str(terreno), "Test Terreno")


class CatalogoViewTest(TestCase):
    def test_catalogo_view_returns_200(self):
        response = self.client.get("/catalogo/")
        self.assertEqual(response.status_code, 200)

    def test_catalogo_view_uses_correct_template(self):
        response = self.client.get("/catalogo/")
        self.assertTemplateUsed(response, "base.html")
