# My Meralco Streamlit prototype
# Put optional image assets in ./assets as described in README_20261111.txt.

from pathlib import Path
import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(page_title='My Meralco', page_icon='⚡', layout='wide', initial_sidebar_state='collapsed')

ASSET_DIR = Path('assets')
KLARO_URL = 'https://meralco.sharepoint.com/sites/cpiar/Shared%20Documents/Copilot%20Studio%20Agents?id=/sites/cpiar/Shared%20Documents/Copilot%20Studio%20Agents/Klaro_crba2_bill.agent&parent=/sites/cpiar/Shared%20Documents/Copilot%20Studio%20Agents'
CUSTOMER_NAME = 'Juan Dela Cruz'
ACCOUNT_NUMBER = '05852167123'

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login(): st.session_state.logged_in = True
def logout(): st.session_state.logged_in = False

import streamlit.components.v1 as components

st.markdown(
    """
    <style>
        .stApp { background: #fff; }
        div[data-testid="stMain"] > div { padding-top: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML = '''
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>My Meralco + Klaro Demo</title>
<style>
:root{--blue:#21289c;--blue2:#1650aa;--teal:#08b9bc;--aqua:#dff8f8;--orange:#ff6900;--ink:#232436;--muted:#6a6d78;--white:#fff;--line:#d8e2e6}*{box-sizing:border-box}html,body{margin:0;min-height:100%;font-family:'Century Gothic','Avenir Next','Avenir','Trebuchet MS',sans-serif;color:var(--ink);letter-spacing:.01em}body{background:#fff}.page{display:none;min-height:100vh}.page.active{display:flex;flex-direction:column}.brandbar{height:64px;background:#fff;display:flex;align-items:center;justify-content:center}.logo{width:34px;height:34px;border-radius:50%;background:var(--orange);color:white;display:grid;place-items:center;font-weight:900;font-style:italic}.gradient{background:linear-gradient(180deg,#1c359d 0%,#1552aa 47%,#08b9bc 100%);color:#fff}.demo-note{font:10px Arial,sans-serif;color:#fff;background:rgba(0,0,0,.13);text-align:center;padding:7px}.footer{margin-top:auto;padding:14px 20px;text-align:center;font:10px Arial,sans-serif;color:#677}.footer.dark{color:#fff}.landing-main,.login-main{flex:1;width:min(1070px,calc(100% - 36px));margin:auto;display:grid;grid-template-columns:1.05fr .95fr;gap:55px;align-items:center;padding:35px 0}.welcome h1{font-size:52px;line-height:1.4;font-weight:500;margin:0 0 20px}.welcome p{font-size:23px;line-height:1.6;margin:0;max-width:560px}.welcome .small{font-size:13px;margin-top:25px;color:#e9ffff}.visuals{height:300px;position:relative}.circle{position:absolute;border-radius:50%;background:#fff;box-shadow:0 15px 28px #1236}.circle.big{width:235px;height:235px;right:30px;top:0;border:3px solid #ff5977}.circle.small{width:105px;height:105px;right:60px;bottom:0;border:3px solid #91c600}.circle:before{content:'⚡';display:grid;place-items:center;height:100%;font-size:55px;color:#ff6900}.circle.big:before{content:'My Meralco';font-size:20px;color:#2544a5}.access,.loginbox{background:linear-gradient(#fff,#d9f7f8);border-radius:16px;padding:45px 52px;box-shadow:0 12px 30px #1234;color:#232436}.access p,.loginbox p{font-size:14px;color:#2f3440}.btn{font-family:inherit;border:0;border-radius:9px;min-height:54px;width:100%;font-weight:700;margin:7px 0;cursor:pointer}.navy{background:#20249e;color:#fff}.teal{background:#09b8bc;color:white}.outline{background:transparent;color:#2443ad;border:2px solid #2443ad}.orange{background:#ff6900;color:#fff}.download{background:#fff;border-radius:15px;padding:22px;margin-top:18px;color:#414652;font-size:12px;box-shadow:0 8px 22px #1232}.loginbox{padding:43px 48px}.loginbox h2{text-align:center;font-size:17px;font-weight:500;margin:0 0 35px;color:#232436}.logincols{display:grid;grid-template-columns:1fr 1px 1fr;gap:20px}.divider{background:#13c0c5}.field label{font-size:13px;display:block;margin:0 0 6px;color:#4a4f5c}.field input{height:43px;width:100%;border:1px solid #aeb4be;padding:10px 12px;font-family:inherit;background:#fff;color:#232436;box-shadow:inset 0 1px 4px #0001}.field input::placeholder{color:#777f8c;opacity:1}.remember{font-size:11px;margin:12px 0 20px;display:flex;justify-content:space-between;gap:12px;color:#4a4f5c}.remember a,.create-link a{color:#243fab}.sso .btn{background:#fff;border:0;color:#31323b;box-shadow:0 1px 4px #0001}.sso .facebook{background:#1877ed;color:white}.sso .apple{background:#17181d;color:white}.create-link{text-align:center;font-size:12px;margin-top:20px;color:#4a4f5c}.pageback{position:fixed;left:18px;top:78px;z-index:30;border:1px solid #ffffff88;background:#ffffffee;color:#25299b;border-radius:999px;padding:9px 14px;font-family:inherit;font-weight:700;cursor:pointer;box-shadow:0 4px 14px #0002}.pageback.dark{border-color:#d7dbe7;background:#fff}.error{min-height:18px;color:#b42318;font:11px Arial,sans-serif;margin-top:4px}.appnav{height:64px;background:#fff;display:flex;align-items:center;justify-content:center;gap:60px;color:#272a9a;font-size:14px}.appnav a{color:inherit;text-decoration:none}.appnav .active{font-weight:800;border-bottom:3px solid #04b9bc;padding:20px 0}.appnav .logo{margin:0 8px}.dashHero{background:linear-gradient(180deg,#173797,#1752a4 52%,#08b9bc);height:358px;color:#fff}.dashwrap{width:min(900px,calc(100% - 36px));margin:auto;display:grid;grid-template-columns:1.55fr .75fr;gap:35px;padding-top:24px}.hello h1{font-size:27px;margin:0 0 15px}.hello p{font-size:13px;line-height:1.8}.learn{width:280px;height:38px;border:2px solid #fff;background:transparent;color:#fff;border-radius:5px;font-family:inherit;font-weight:700}.account{background:linear-gradient(#fff,#ddf7f7);color:#27295e;border-radius:15px;padding:27px;box-shadow:0 14px 28px #1233}.account h3{margin:0 0 15px}.account .num{font-size:13px;font-weight:800;color:#24279d}.amount{border:1px solid #11bec2;border-radius:10px;background:#fff;padding:12px;text-align:right;margin:20px 0;color:#bbb;font-size:12px}.amount strong{font-size:28px}.klaro-link{display:flex;align-items:center;justify-content:center;text-decoration:none}.klaro-float{position:fixed;right:28px;bottom:56px;z-index:15;display:flex;align-items:center;gap:10px;padding:14px 20px;border-radius:999px;background:#ff6900;color:#fff;text-decoration:none;font-weight:800;box-shadow:0 10px 28px rgba(255,105,0,.35);border:2px solid #fff}.klaro-float:hover{filter:brightness(.97);transform:translateY(-1px)}.klaro-float .kicon{width:30px;height:30px;border-radius:50%;background:#fff;color:#ff6900;display:grid;place-items:center;font-weight:900}.dashboardBody{width:min(900px,calc(100% - 36px));margin:-100px auto 40px;display:grid;grid-template-columns:1.55fr .75fr;gap:35px}.energy{background:#fff;border-radius:15px;box-shadow:0 5px 18px #0002;padding:25px 45px;min-height:420px}.energy h2{text-align:center;color:#292c9a;font-size:20px;line-height:1.5}.kwh{text-align:center;font-size:22px;color:#292c9a;margin:35px 0 10px}.kwh small{display:block;color:#666;font-size:10px;margin-top:8px}.chart{height:130px;display:flex;align-items:end;justify-content:center;gap:18px;margin-top:35px}.bar{width:18px;background:#02b6b8;border-right:7px solid #163aa9}.sidecards{display:grid;gap:20px}.promo{background:#f0f0f0;border-radius:14px;padding:24px;color:#252991;min-height:180px}.promo strong{font-size:18px}.dashfoot{background:#eee;padding:16px;text-align:center;font:9px Arial;color:#777;margin-top:auto}.success{position:fixed;inset:0;background:#1236;display:none;place-items:center;z-index:20}.success.show{display:grid}.successbox{background:#fff;border-radius:14px;padding:25px 35px;text-align:center;box-shadow:0 15px 40px #0004}.successbox .spinner{width:26px;height:26px;border:3px solid #ddd;border-top-color:#08b9bc;border-radius:50%;margin:0 auto 12px;animation:spin .7s linear infinite}@keyframes spin{to{transform:rotate(360deg)}}
@media(max-width:850px){.landing-main,.login-main,.dashwrap,.dashboardBody{grid-template-columns:1fr}.visuals{display:none}.appnav{gap:18px;font-size:11px;overflow:auto}.dashHero{height:auto;padding-bottom:130px}.dashboardBody{margin-top:-110px}.welcome h1{font-size:38px}.welcome p{font-size:18px}.logincols{grid-template-columns:1fr}.divider,.sso{display:none}.account{margin-top:20px}}
</style>
</head>
<body>
<section id="landing" class="page active gradient">
<header class="brandbar"><div class="logo">M</div></header>
<div class="landing-main">
<div>
<div class="visuals"><div class="circle big"></div><div class="circle small"></div></div>
<div class="welcome"><h1>Welcome to<br>My Meralco</h1><p>View and Pay Bills, Report Brownouts, Billing Alerts, Apply for Electric Service and more...</p><p class="small">A redesigned demonstration experience inspired by My Meralco.</p></div>
</div>
<div>
<div class="access"><p>Log in to your account</p><button class="btn navy" onclick="go('login')">Log in</button><p>Don't have an account?</p><button class="btn teal" onclick="demo('Create Account')">Create Account</button><button class="btn outline" onclick="demo('Continue as Guest')">Continue as Guest</button></div>
<div class="download">⚡ &nbsp; Download My Meralco to manage your account conveniently anytime, anywhere.</div>
</div>
</div>
<div class="demo-note">MOCK WEBSITE FOR DEMONSTRATION PURPOSES ONLY. No real account, billing, payment, or authentication transaction is performed.</div>
<footer class="footer dark">© My Meralco 2026 &nbsp; | &nbsp; Terms and Conditions &nbsp; | &nbsp; Privacy Statement</footer>
</section>
<section id="login" class="page gradient">
<button class="pageback" type="button" onclick="backPage()">← Back</button>
<header class="brandbar"><div class="logo">M</div></header>
<div class="login-main">
<div class="welcome"><h1>Welcome to<br>My Meralco</h1><p>View and Pay Bills, Report Brownouts, Billing Alerts, Apply for Electric Service and more...</p></div>
<div class="loginbox"><h2>Log in to your account</h2><div class="logincols"><div><div class="field"><label>Username</label><input id="user" autocomplete="off" placeholder="Enter any demo username"></div><div class="field" style="margin-top:16px"><label>Password</label><input id="pass" type="password" placeholder="Enter any demo password"></div><div class="remember"><label><input type="checkbox"> Remember Me</label><a href="javascript:void(0)" onclick="demo('Forgot Password')">Forgot Password</a></div><button class="btn navy" onclick="login()">Log in</button><div id="error" class="error"></div></div><div class="divider"></div><div class="sso"><p>Or log in with Single Sign-On</p><button class="btn facebook" onclick="loginSSO()">● &nbsp; Log in with Facebook</button><button class="btn" onclick="loginSSO()">G &nbsp; Log in with Google</button><button class="btn apple" onclick="loginSSO()">● &nbsp; Log in with Apple</button></div></div><div class="create-link">Don't have an account?<br><a href="javascript:void(0)" onclick="demo('Create Account')">Create Account</a></div></div>
</div>
<div class="demo-note">MOCK LOGIN FOR DEMONSTRATION PURPOSES ONLY. Enter any non-empty demo username and password. Do not enter real credentials.</div>
<footer class="footer dark">© My Meralco 2026 &nbsp; | &nbsp; Terms and Conditions &nbsp; | &nbsp; Privacy Statement</footer>
</section>
<section id="dashboard" class="page">
<button class="pageback dark" type="button" onclick="backPage()">← Back</button>
<nav class="appnav"><a class="active" href="javascript:void(0)">Dashboard</a><a href="javascript:void(0)" onclick="demo('Billings')">Billings</a><a href="javascript:void(0)" onclick="demo('Accounts')">Accounts</a><div class="logo">M</div><a href="javascript:void(0)" onclick="demo('Brownouts')">Brownouts</a><a href="javascript:void(0)" onclick="demo('Help & Support')">Help & Support</a><a href="javascript:void(0)" onclick="logout()">Log out</a></nav>
<div class="dashHero"><div class="dashwrap"><div class="hello"><h1>Hello Maria,</h1><p>Welcome to the new My Meralco<br>Stay tuned for more features<br>coming soon</p><button class="learn" onclick="demo('Learn more')">Learn more</button></div><div class="account"><h3>⌂ House</h3><div style="font-size:10px">Customer Account Number</div><div class="num">1245031385</div><div class="amount">Current amount due<br><strong>₱ 3,842.17</strong></div><button class="btn navy" onclick="demo('Pay in Advance')">⚡ Pay in Advance</button><button class="btn outline" onclick="demo('View Payment History')">▤ View Payment History</button></div></div></div>
<div class="dashboardBody"><div class="energy"><h2>Your monthly<br>energy consumption</h2><div class="kwh"><strong>103.00</strong> kWh<small>Actual Consumption<br>1% higher from previous.</small></div><div class="chart"><div class="bar" style="height:90px"></div><div class="bar" style="height:84px"></div><div class="bar" style="height:75px"></div><div class="bar" style="height:88px"></div><div class="bar" style="height:96px"></div><div class="bar" style="height:91px"></div><div class="bar" style="height:82px"></div><div class="bar" style="height:85px"></div><div class="bar" style="height:78px"></div><div class="bar" style="height:73px"></div></div></div><div class="sidecards"><div class="promo">Tired of retyping your payment details on My Meralco?<br><br><strong>Skip the hassle.</strong></div><div class="promo"><strong>Klaro</strong><br><br>Need help understanding your electricity bill?<br><a class="btn orange klaro-link" style="margin-top:18px" href="https://meralco.sharepoint.com/sites/cpiar/Shared%20Documents/Copilot%20Studio%20Agents?id=/sites/cpiar/Shared%20Documents/Copilot%20Studio%20Agents/Klaro_crba2_bill.agent&parent=/sites/cpiar/Shared%20Documents/Copilot%20Studio%20Agents" target="_blank" rel="noopener noreferrer">Ask Klaro</a></div></div></div>
<a class="klaro-float" href="https://meralco.sharepoint.com/sites/cpiar/Shared%20Documents/Copilot%20Studio%20Agents?id=/sites/cpiar/Shared%20Documents/Copilot%20Studio%20Agents/Klaro_crba2_bill.agent&parent=/sites/cpiar/Shared%20Documents/Copilot%20Studio%20Agents" target="_blank" rel="noopener noreferrer" title="Open Klaro"><span class="kicon">K</span><span>Ask Klaro</span></a>
<div class="demo-note" style="background:#737373;color:white">MOCK WEBSITE FOR DEMONSTRATION PURPOSES ONLY. Displayed account, consumption, and billing information are fictional sample data.</div>
<footer class="dashfoot">© My Meralco 2026. All Rights Reserved &nbsp; &nbsp; Terms & Conditions &nbsp; &nbsp; Privacy Notice &nbsp; &nbsp; Submit Feedback</footer>
</section>
<div id="success" class="success"><div class="successbox"><div class="spinner"></div>Logging in to My Meralco...</div></div>
<script>
function go(id){document.querySelectorAll('.page').forEach(function(p){p.classList.remove('active')});var target=document.getElementById(id);if(target){target.classList.add('active');window.scrollTo(0,0)}}
function backPage(){var dash=document.getElementById('dashboard');var loginPage=document.getElementById('login');if(dash.classList.contains('active')){go('login')}else if(loginPage.classList.contains('active')){go('landing')}else{go('landing')}}
function demo(x){alert(x+' is included for demonstration only.')} 
function login(){const u=document.getElementById('user').value.trim(),p=document.getElementById('pass').value.trim();if(!u||!p){document.getElementById('error').textContent='Enter a demo username and password to continue.';return}document.getElementById('error').textContent='';const s=document.getElementById('success');s.classList.add('show');setTimeout(()=>{s.classList.remove('show');go('dashboard')},650)}
function loginSSO(){document.getElementById('success').classList.add('show');setTimeout(()=>{document.getElementById('success').classList.remove('show');go('dashboard')},650)}
function logout(){go('landing')}
</script>
</body>
</html>
'''

components.html(HTML, height=1200, scrolling=True)
