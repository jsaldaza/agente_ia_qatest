# 🤖 IA-Powered Test Case Generator + Playwright Automation

![CI](https://github.com/jsaldaza/agente_ia_qatest/actions/workflows/playwright-tests.yml/badge.svg)

Este proyecto combina Inteligencia Artificial y Automatización de Pruebas para transformar...


Este proyecto combina Inteligencia Artificial y Automatización de Pruebas para transformar historias de usuario en escenarios BDD automatizables con Playwright y Python. Diseñado como una herramienta realista para equipos QA y desarrolladores.

---

## 🚀 Características principales

- Generador IA que recibe historias de usuario y genera:
  - Casos de prueba manuales.
  - Escenarios BDD (Gherkin).
- Exportación automática a:
  - `.md` (documentación)
  - `.csv` (excel para QA manual)
  - `.feature` (para pruebas automatizadas)
- Automatización real con Playwright + Python + Pytest-BDD
- Patrón de diseño **Page Object Model**
- Sitio base: [Automation Practice](http://www.automationpractice.pl/index.php)

---

## 🧠 Tecnologías y herramientas

- Python 3.12+
- OpenAI API
- Playwright
- Pytest + Pytest-BDD
- Page Object Model (POM)
- Markdown + CSV + Gherkin

---

## 📁 Estructura del proyecto

```bash
agente_ia_qatest/
├── features/               # Escenarios .feature generados por IA
│   └── testcases_*.feature
├── outputs/                # Exportaciones .md y .csv
├── pages/                  # Page Object Model (HomePage)
│   └── home_page.py
├── tests/
│   └── steps/           # Glue code (pytest-bdd)
│       └── test_busqueda_steps.py
├── conftest.py             # Configuración de navegador (Playwright)
├── main.py                 # Script principal: entrada de historia + generación
├── requirements.txt
└── .env                    # Clave segura de OpenAI
```

---

## 🧪 Ejecución de pruebas automatizadas

```bash
# Crear entorno virtual y activarlo
python -m venv .venv
.venv\Scripts\activate      # En Windows

# Instalar dependencias
pip install -r requirements.txt
python -m playwright install

# Ejecutar generador IA
python main.py

# Ejecutar pruebas automatizadas
pytest tests/
```

---

## ✅ Escenario automatizado actual

**Historia de Usuario:**
> Como cliente, quiero poder buscar un producto por nombre en el campo de búsqueda, para encontrarlo rápidamente dentro del catálogo online.

**Escenarios generados y automatizados:**
- Buscar producto existente ("dress") y validar resultados.
- Buscar producto inexistente ("nonexistentproduct") y validar mensaje de error.

---

## ✨ Autor

**Juan Andrés Saldarriaga Zapata**  
QA Engineer | Automation | Continuous Improver  
[GitHub](https://github.com/jsaldaza) • [LinkedIn](https://linkedin.com/in/jsaldaza) • [Blog](https://jsaldaza.hashnode.dev)

---

## 🪄 Ideas futuras

- Generar scripts Cypress o Playwright directo desde Gherkin
- Subir resultados a Notion o Jira
- Integrar con GitHub Actions para CI/CD
- Exportar reportes Allure o HTML

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo libremente para fines educativos o profesionales. ✨

