"""
Script de prueba rápida para verificar que todos los endpoints funcionan correctamente
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_endpoint(endpoint_name, url):
    """Prueba un endpoint y muestra el resultado"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"✅ {endpoint_name}: OK")
            return True
        else:
            print(f"❌ {endpoint_name}: Error {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ {endpoint_name}: {str(e)}")
        return False

def main():
    print("🧪 Probando API de Fardo...\n")
    
    endpoints = [
        ("Root", f"{BASE_URL}/"),
        ("Health Check", f"{BASE_URL}/health"),
        ("Company", f"{BASE_URL}/company"),
        ("Services", f"{BASE_URL}/services"),
        ("Plans", f"{BASE_URL}/plans"),
        ("Team", f"{BASE_URL}/team"),
        ("Methodology", f"{BASE_URL}/methodology"),
        ("Roadmap", f"{BASE_URL}/roadmap"),
        ("FAQs", f"{BASE_URL}/faq"),
        ("Glossary", f"{BASE_URL}/glossary"),
        ("AI Engines", f"{BASE_URL}/ai-engines"),
        ("Value Propositions", f"{BASE_URL}/value-propositions"),
        ("Industry Benchmarks", f"{BASE_URL}/industry-benchmarks"),
        ("Resources", f"{BASE_URL}/resources"),
        ("Comparison", f"{BASE_URL}/comparison"),
        ("Updates", f"{BASE_URL}/updates"),
        ("Search", f"{BASE_URL}/search?q=AEO"),
    ]
    
    results = []
    for name, url in endpoints:
        results.append(test_endpoint(name, url))
    
    print(f"\n📊 Resultados: {sum(results)}/{len(results)} endpoints funcionando correctamente")
    
    if all(results):
        print("\n🎉 ¡Todos los endpoints están funcionando!")
    else:
        print("\n⚠️  Algunos endpoints tienen problemas. Revisa el servidor.")

if __name__ == "__main__":
    print("Asegúrate de que el servidor esté corriendo en http://localhost:8000")
    print("Ejecuta: uvicorn main:app --reload\n")
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Prueba cancelada")

