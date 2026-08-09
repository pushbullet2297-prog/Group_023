Mobile Price Prediction - Streamlit App Bundle
================================================

Files in this folder:
- app.py                  -> the Streamlit app
- mobile_price_model.pkl  -> trained Random Forest model
- scaler.pkl              -> fitted StandardScaler (must match the model)
- feature_columns.pkl     -> exact column order the model expects

HOW TO RUN
----------
1. Make sure all 4 files above are in the SAME folder (don't separate them).
2. Open a terminal in that folder.
3. Install Streamlit (only needed once):
       pip install streamlit
4. Launch the app:
       streamlit run app.py
5. It will open automatically in your browser (usually http://localhost:8501).
   Fill in the phone specs on the form and click "Predict" to see the
   predicted price range (0 = cheapest ... 3 = most expensive).

NOTES
-----
- Do not rename any of the .pkl files - app.py loads them by these exact names.
- If "streamlit" command isn't recognized after installing, try:
       python -m streamlit run app.py
- This app expects Python 3.9+ with scikit-learn and joblib installed
  (both come in automatically as dependencies of scikit-learn/streamlit
  install, but if you get an import error, run: pip install scikit-learn joblib)
