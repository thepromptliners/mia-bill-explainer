MY MERALCO STREAMLIT PROTOTYPE

Suggested folder structure:

my_meralco_app/
|-- app_20261111.py
|-- requirements_20261111.txt
`-- assets/
    |-- login_family.png
    |-- login_meter.png
    |-- feedback.png
    `-- bayad_express.png

The image assets are optional. The app runs without them and shows a fallback graphic.

SETUP
1. Create the folder my_meralco_app.
2. Copy app_20261111.py and requirements_20261111.txt into it.
3. Create the assets folder.
4. Add your own authorized images using the filenames above, if desired.
5. Install dependencies:
   pip install -r requirements_20261111.txt
6. Run:
   streamlit run app_20261111.py

Notes:
- The dashboard data is prototype/static data.
- Klaro currently opens through its existing SharePoint URL.
- For production, move customer/account data to an authenticated backend instead of hard-coding it in the UI.
