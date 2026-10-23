#!/usr/bin/env python3
"""
Script de verificación para CVE eMudhra (oct 2026).
Verifica que el bundle de CA rechace certificados firmados por CAs comprometidas.

Hosts de prueba (certificados firmados con claves comprometidas de eMudhra):
  - https://dv-g3b-emudhra.we-have-a-problem.com/
  - https://dv-g3b-aaa-emudhra.we-have-a-problem.com/

Lo esperado es un error SSL/certificado en ambos casos.
"""

import ssl
import urllib.request
import urllib.error
import sys

TEST_HOSTS = [
    "https://dv-g3b-emudhra.we-have-a-problem.com/",
    "https://dv-g3b-aaa-emudhra.we-have-a-problem.com/",
]

def check_host(url: str) -> tuple[str, bool]:
    """
    Intenta conectarse al host por HTTPS.
    Retorna (mensaje, ok) donde ok=True si la conexión FALLA con error SSL (comportamiento esperado).
    """
    try:
        ctx = ssl.create_default_context()
        with urllib.request.urlopen(url, timeout=10, context=ctx) as resp:
            return (f"FALLA - conexión exitosa (status {resp.status}), debería haber fallado SSL", False)
    except ssl.SSLCertVerificationError as e:
        return (f"OK - error de verificación SSL: {e.reason}", True)
    except ssl.SSLError as e:
        return (f"OK - error SSL: {e}", True)
    except urllib.error.URLError as e:
        if isinstance(e.reason, ssl.SSLError):
            return (f"OK - error SSL: {e.reason}", True)
        if isinstance(e.reason, ssl.SSLCertVerificationError):
            return (f"OK - error de verificación SSL: {e.reason}", True)
        return (f"ERROR - error de red (no SSL): {e.reason}", False)
    except Exception as e:
        return (f"ERROR - excepción inesperada: {type(e).__name__}: {e}", False)

def main() -> int:
    print("=" * 60)
    print("Verificación eMudhra CA Trust Store")
    print("=" * 60)
    print()

    all_ok = True
    for url in TEST_HOSTS:
        host = url.replace("https://", "").rstrip("/")
        msg, ok = check_host(url)
        status = "✓" if ok else "✗"
        print(f"[{status}] {host}")
        print(f"    {msg}")
        print()
        if not ok:
            all_ok = False

    print("=" * 60)
    if all_ok:
        print("Resultado: PASS - Todos los hosts rechazados correctamente")
    else:
        print("Resultado: FAIL - Algún host no fue rechazado")
    print("=" * 60)

    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
