# Marketing Campaign Performance Analysis 📈

## 1. ¿Qué problema resuelve?
En el ecosistema del marketing digital, las empresas suelen enfrentarse al "ruido" de los datos: grandes volúmenes de información provenientes de múltiples canales (Social Media, Email, Influencers) que no siempre se traducen en decisiones claras.

Este proyecto resuelve la falta de visibilidad estratégica para la agencia ficticia **Nexus Solutions**. El análisis permite transformar 200,000 registros de campañas en insights accionables, respondiendo a preguntas críticas de negocio como:

* **Optimización de Presupuesto:** ¿Qué canales están quemando dinero con un ROI negativo y cuáles merecen más inversión?
* **Eficiencia de Adquisición:** ¿Cuál es el costo real de adquirir un cliente (CAC) en diferentes segmentos?
* **Segmentación de Precisión:** ¿Qué combinación de idioma, ubicación y tipo de audiencia genera la mayor tasa de conversión?
* **Predicción de Engagement:** ¿Existe una correlación real entre la duración de la campaña y el éxito de la misma?

El objetivo es pasar de una gestión reactiva a una **estrategia basada en datos (Data-Driven)** para maximizar la rentabilidad de cada dólar invertido.

---

## 2. Stack Técnico Usado

Para este proyecto se optó por una arquitectura **ELT (Extract, Load, Transform)**, priorizando la integridad de los datos y la potencia de procesamiento del motor de base de datos.

| Herramienta | Función |
| :--- | :--- |
| **Python (Pandas)** | **Extracción y Carga:** Utilizado para la ingesta del dataset desde Kaggle y la carga inicial (Raw Data) hacia la base de datos. |
| **PostgreSQL** | **Almacenamiento y Transformación:** El motor principal donde se realiza la limpieza, el modelado de datos y el cálculo de métricas complejas mediante SQL (Views/Common Table Expressions). |
| **Power BI** | **Visualización y BI:** Creación de dashboards interactivos, modelado de datos (Star Schema) y reporting para la toma de decisiones ejecutivas. |
| **SQL** | **Lógica de Negocio:** Desarrollo de scripts para transformar datos crudos en tablas de hechos y dimensiones (Capa Gold). |