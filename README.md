# 🛠️ AutomateLI – Automatización de Lista de Instrumentos (LI)

**Autor:** J. Livramento  
**Repositorio:** [AutomateLI](https://github.com/javilivra/AutomateLI) *(nombre tentativo del repo si lo renombrás)*  
**Estado:** 🔧 *En construcción – documentación preliminar*

---

## 📌 Objetivo del Proyecto

Desarrollar un sistema robusto de automatización técnica mediante **Visual Basic for Applications (VBA)** para completar de forma automática la **Lista de Instrumentos (LI)** usada en ingeniería de Instrumentación & Control, a partir de la extracción de atributos desde archivos AutoCAD (DWG).

---

## ⚙️ Tecnologías utilizadas

- **Visual Basic for Applications (VBA)** para macros en Excel
- **AutoCAD (bloques DWG)** como fuente de datos
- **Plantillas Excel** estandarizadas para Ingeniería de I&C

> 🔄 En el futuro se integrará con herramientas como Python y N8N para versiones multiplataforma.

---

## 📁 Estructura del repositorio

```bash
AutomateLI/
├── Macros/           # Código fuente en VBA (.bas)
├── Docs/             # Documentación técnica, flujos y manuales
├── scripts_python/   # (en desarrollo) futuras integraciones externas
└── README.md         # Manual del usuario (versión preliminar)

```

## 🐍 Entorno Python para scripts

Los scripts en `scripts_python/` requieren Python 3 y la biblioteca `ezdxf`.
Sigue estos pasos para preparar el entorno:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Después puedes ejecutar los scripts desde esa consola activa.
