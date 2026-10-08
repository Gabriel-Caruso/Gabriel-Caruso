<div align="center">
  <img src="header.png" alt="Header" width="900">
</div>

<!-- Blinking Cursor Typing SVG -->
<div align="center">

[![Terminal](https://readme-typing-svg.demolab.com?font=Fira%20Code&weight=600&size=22&pause=1000&color=FFB000&center=true&vCenter=true&multiline=false&repeat=false&width=1000&height=50&lines=AVAILABLE%20FOR%20HIRE%20%C2%B7%20JUNIOR%20DATA%20SCIENTIST%20%2F%2F%20DATA%20ANALYST)](https://git.io/typing-svg)

</div>


<div align="center">

<img src="AboutMe_button.png" alt="About me" width="900">

</div>

<div align="center">
  <img src="about_me.jpg" alt="Ramiro Gabriel Caruso: Junior Data Scientist y Data Analyst en Oviedo, disponible para trabajar en remoto" width="900">
</div>

---

<div align="center">

<img src="FeaturedProjects_button.png" alt="Featured projects" width="900">

</div>

### Telco churn: predicción de bajas de clientes
**ML end-to-end en Databricks: de un CSV en bruto a una app pública que dice a quién llamar primero**

<table>
  <tr>
    <td width="50%"><a href="https://telco-churn-ramiro-caruso.streamlit.app/"><img src="churn_app.png" alt="App de Telco churn en Streamlit"></a></td>
    <td width="50%"><a href="https://telco-churn-ramiro-caruso.streamlit.app/"><img src="churn_eda.png" alt="Tasa de baja en fibra según servicios extra contratados"></a></td>
  </tr>
</table>

> **PR-AUC 0,635 (un modelo al azar: 0,265) · lista mensual de 806 clientes en riesgo · 37 tests**

**El problema:** una operadora pierde al 26,5 % de sus clientes. El equipo de retención no puede llamar a todos, así que necesita saber a quién contactar primero. El modelo, entrenado con 7043 clientes del dataset IBM Telco, ordena a los clientes actuales por probabilidad de baja.

```text
CSV ─► bronze ─► silver ─► gold ─► MLflow (CV 5 folds) ─► Unity Catalog [champion]
                                                              ├─► batch scoring
                                                              ├─► endpoint REST
                                                              └─► app Streamlit
```

- **Desarrollado en Databricks:** capas bronze, silver y gold en tablas Delta de Unity Catalog, con validación en cada capa y features en un paquete propio con tests (la misma función entrena, puntúa y alimenta la app).
- **Modelado:** regresión logística frente a random forest, gradient boosting y XGBoost ajustados, comparados en MLflow. Los challengers solo ganan ~0,02 de PR-AUC, dentro del ruido entre folds, así que se mantiene la logística porque es explicable.
- **Decisión de negocio:** PR-AUC por el desbalanceo y un umbral de 0,40 elegido por el coste de cada baja detectada.
- **Hallazgos clave:** el 62 % de las bajas llegan en el primer mes, y la fibra contratada sola es el problema (60 % de bajas sin servicios extra frente al 9 % con los seis).
- **Producción:** modelo registrado con el alias `champion`, batch scoring a tabla, endpoint REST con Model Serving y app bilingüe con explicación de cada predicción.

[![App en vivo](https://img.shields.io/badge/APP_EN_VIVO-Pru%C3%A9bala-ffb000?style=flat-square&labelColor=000000)](https://telco-churn-ramiro-caruso.streamlit.app/)  
[![Repo](https://img.shields.io/badge/REPO-telco--churn--prediction-ffb000?style=flat-square&logo=github&logoColor=ffb000&labelColor=000000)](https://github.com/Gabriel-Caruso/telco-churn-prediction)  

`Python · Databricks · MLflow · Unity Catalog · Delta Lake · scikit-learn · Streamlit · pytest`  

<sub>Si la app lleva tiempo sin visitas, Streamlit la duerme: pulsa el botón para despertarla y espera unos segundos.</sub>

---

### Tasador de vivienda en Madrid
**ML end-to-end: de anuncios scrapeados en bruto a una API REST pública**

[![Tasador](tasador.png)](https://ml-vivienda-madrid.onrender.com/)

> **R² 0,86 · ~16 % de error medio en el 80 % del mercado · −49 % de error frente al baseline**

Predice el precio de venta de una vivienda en Madrid a partir de los datos de su anuncio (11,8k anuncios de Idealista).

- **Limpieza de datos:** valores centinela, NaNs estructurales frente a faltantes reales, duplicados ocultos eliminados con una clave de 9 campos y más de 50 variables extraídas de las etiquetas de texto libre.
- **Modelado:** Baseline lineal frente a XGBoost, LightGBM y CatBoost, con split estratificado por distrito y ajuste con Optuna. Ganador: CatBoost.
- **Hallazgo clave:** la ingeniería de variables (barrio + etiquetas) redujo el error 10 veces más que el ajuste de hiperparámetros.
- **Despliegue:** FastAPI en Render, con validación de entradas, GET/POST `/predict` y documentación interactiva con Swagger.

[![API en vivo](https://img.shields.io/badge/API_EN_VIVO-Pru%C3%A9bala-ffb000?style=flat-square&labelColor=000000)](https://ml-vivienda-madrid.onrender.com/)  
[![Repo modelo](https://img.shields.io/badge/REPO-ML--idealista-ffb000?style=flat-square&logo=github&logoColor=ffb000&labelColor=000000)](https://github.com/Gabriel-Caruso/ML-idealista)  
[![Repo API](https://img.shields.io/badge/REPO-API-ffb000?style=flat-square&logo=fastapi&logoColor=ffb000&labelColor=000000)](https://github.com/A-Manz/TCH-5-Despliegue/tree/develop)  

`Python · CatBoost · Optuna · scikit-learn · FastAPI · Render`  

<sub>Proyecto en equipo con Ana Manzanares. Me encargué de la limpieza de datos, el modelado y la optimización. La primera petición puede tardar ~1 min porque el servidor gratuito arranca en frío.</sub>


---


<div align="center">
  
## ▓▒░ SYSTEMS & TECHNOLOGIES ░▒▓

**LANGUAGES**  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge) ![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)

**DATA / ML**  
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge) ![CatBoost](https://img.shields.io/badge/CatBoost-FFCC00?style=for-the-badge) ![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)

**DEPLOY**  
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

**CLOUD / DATA**  
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white) ![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

**TOOLS**  
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

</div>

---

<div align="center">
  <img src="skills.jpg" alt="Competencias: Python, pandas, NumPy, scikit-learn y SQL sólidos; Git a diario; Azure en uso; Databricks aprendiendo" width="900">
</div>

---


<div align="center">

## ▓▒░ SYSTEM DIAGNOSTICS ░▒▓

</div>

<div align="center">

<img height="180em" src="https://github-stats-extended.vercel.app/api?username=gabriel-caruso&show_icons=true&bg_color=000000&text_color=ffb000&icon_color=ffb000&title_color=ffb000&hide_border=true&count_private=true" alt="BBS Stats" />
<img height="180em" src="https://github-stats-extended.vercel.app/api/top-langs/?username=gabriel-caruso&layout=compact&bg_color=000000&text_color=ffb000&icon_color=ffb000&title_color=ffb000&hide_border=true&langs_count=8" alt="Phosphor Langs" />

</div>

<br>

<div align="center">

[![BBS Streak](https://streak-stats.demolab.com?user=gabriel-caruso&background=000000&ring=ffb000&fire=ffb000&currNo=ffb000&currLeft=ffb000&sideNums=ffb000&sideLabels=ffb000&dates=ffb000&hide_border=true)](https://git.io/streak-stats)

</div>

---

<div align="center">
  
## ▓▒░ PROJECTS MAINTAINED ░▒▓

</div>

<div align="center">

<table cellspacing="10" cellpadding="0" border="0">
  <tr>
    <td>
      <a href="https://github.com/gabriel-caruso/telco-churn-prediction">
        <img src="https://github-stats-extended.vercel.app/api/pin/?username=gabriel-caruso&repo=telco-churn-prediction&bg_color=000000&text_color=ffb000&icon_color=ffb000&title_color=ffb000&hide_border=true&description_lines_count=1" alt="ReadMe Card" width="400" height="120" />
      </a>
    </td>
    <td>
      <a href="https://github.com/gabriel-caruso/ML-idealista">
        <img src="https://github-stats-extended.vercel.app/api/pin/?username=gabriel-caruso&repo=ML-idealista&bg_color=000000&text_color=ffb000&icon_color=ffb000&title_color=ffb000&hide_border=true&description_lines_count=1" alt="ReadMe Card" width="400" height="120" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/gabriel-caruso/DS-Online-Ramiro-Caruso">
        <img src="https://github-stats-extended.vercel.app/api/pin/?username=gabriel-caruso&repo=DS-Online-Ramiro-Caruso&bg_color=000000&text_color=ffb000&icon_color=ffb000&title_color=ffb000&hide_border=true&description_lines_count=1" alt="ReadMe Card" width="400" height="120" />
      </a>
    </td>
    <td>
      <a href="https://github.com/gabriel-caruso/Hundir-la-flota">
        <img src="https://github-stats-extended.vercel.app/api/pin/?username=gabriel-caruso&repo=Hundir-la-flota&bg_color=000000&text_color=ffb000&icon_color=ffb000&title_color=ffb000&hide_border=true&description_lines_count=1" alt="ReadMe Card" width="400" height="120" />
      </a>
    </td>
  </tr>
</table>

</div>

---

<div align="center">

## ▓▒░ ESTABLISH CONTACT ░▒▓

[![GitHub](https://img.shields.io/badge/GitHub-ffb000?style=flat-square&logo=github&logoColor=000000&labelColor=000000)](https://github.com/gabriel-caruso) [![LinkedIn](https://img.shields.io/badge/LinkedIn-ffb000?style=flat-square&logo=linkedin&logoColor=000000&labelColor=000000)](https://www.linkedin.com/in/ramiro-caruso-964899125) [![Twitter](https://img.shields.io/badge/Twitter-ffb000?style=flat-square&logo=twitter&logoColor=000000&labelColor=000000)](https://x.com/Gabrien_)

</div>

---
