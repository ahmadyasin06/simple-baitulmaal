import streamlit as st
import re

# ─────────────────────────────────────────────
#  CONFIG
# ─────────────────────────────────────────────
st.set_page_config(page_title="Shadman Town Bait ul Maal", page_icon="🕌", layout="wide")

# ─────────────────────────────────────────────
#  ✏️  STEP 1 – CHANGE USERNAME & PASSWORD HERE
# ─────────────────────────────────────────────
ADMIN_USERNAME = "ahmadyasin"
ADMIN_PASSWORD = "Jamiat@st123"

# ─────────────────────────────────────────────
#  ✏️  STEP 2 – ADD YOUR ANAT MUAWINEEN HERE
#  Format: {"sr": number, "name": "...", "phone": "...", "address": "...", "amount": number, "notes": "..."}
#  address, amount, notes are optional – leave "" or 0 if not needed
# ─────────────────────────────────────────────
ANAT_MUAWINEEN = [
    {"sr":  1, "name": "Navid Israr",                    "phone": "03343800227", "address": "",       "amount": 500,  "notes": ""},
    {"sr":  1, "name": "Tariq Nisar",                    "phone": "+92 321 2922397", "address": "",       "amount": 1000,  "notes": ""},
    {"sr":  2, "name": "Anas Bhai",                      "phone": "03352482747", "address": "",       "amount": 0,    "notes": ""},
    {"sr":  3, "name": "Musab Tariq",                    "phone": "03161333131", "address": "ONLINE", "amount": 500,  "notes": ""},
    {"sr":  4, "name": "Safdar Zaman",                   "phone": "03333738618", "address": "",       "amount": 500,  "notes": ""},
    {"sr":  5, "name": "Ayehsa Aunty (Asad Bilal Ammi)", "phone": "03222381648", "address": "",       "amount": 1000, "notes": ""},
    {"sr":  6, "name": "Ali Bhai",                       "phone": "-",           "address": "",       "amount": 0,    "notes": ""},
    {"sr":  7, "name": "Umair Talha",                    "phone": "03343131012", "address": "",       "amount": 500,  "notes": ""},
    {"sr":  8, "name": "Fawad Jilani",                   "phone": "03322171456", "address": "",       "amount": 500,  "notes": ""},
    {"sr":  9, "name": "Hafiz Ibrahim Ammi",             "phone": "03142342394", "address": "",       "amount": 500,  "notes": ""},
    {"sr": 10, "name": "Ahsan Jawed",                    "phone": "03212406579", "address": "",       "amount": 500,  "notes": ""},
    {"sr": 11, "name": "Khairul Wara Aunty",             "phone": "03350244138", "address": "",       "amount": 0,    "notes": ""},
    {"sr": 12, "name": "Faseh Uncle",                    "phone": "-",           "address": "",       "amount": 0,    "notes": ""},
    {"sr": 13, "name": "Walee Muhammad Sahab",           "phone": "-",           "address": "",       "amount": 0,    "notes": ""},
    {"sr": 14, "name": "Muneeb Bhai",                    "phone": "03343941620", "address": "",       "amount": 500,  "notes": ""},
    {"sr": 15, "name": "Eras Bhai",                      "phone": "03422578811", "address": "",       "amount": 500,  "notes": ""},
    {"sr": 16, "name": "Tahira Jilani",                  "phone": "-",           "address": "",       "amount": 0,    "notes": ""},
    {"sr": 17, "name": "Saad Bhai",                      "phone": "03249230078", "address": "",       "amount": 500,  "notes": ""},
    {"sr": 18, "name": "Osama Manzar",                   "phone": "03326887571", "address": "",       "amount": 500,  "notes": ""},
    {"sr": 19, "name": "Ahmed",                          "phone": "03350244138", "address": "",       "amount": 0,    "notes": ""},
    {"sr": 20, "name": "Qazi Musab",                     "phone": "03467638419", "address": "",       "amount": 500,  "notes": ""},
    {"sr": 21, "name": "Safeet Ahmed",                   "phone": "03366853138", "address": "",       "amount": 300,  "notes": ""},
    {"sr": 22, "name": "Hanzala Hadeed",                 "phone": "031613322131","address": "",       "amount": 300,  "notes": ""},
]

# ─────────────────────────────────────────────
#  ✏️  STEP 3 – ADD YOUR FUND MUAWINEEN HERE
#  Same format as above
# ─────────────────────────────────────────────
FUND_MUAWINEEN = [
    {"sr": 1, "name": "Raheel Bhai ",     "phone": "+92 331 2000693", "address": "House 3, Shadman Town",   "amount": 1500, "notes": "Anat-1000, 500-Fund"},
    {"sr": 2, "name": "Talha Bhai",    "phone": "+92 332 3561358", "address": "House 7, Block A",        "amount": 1000,  "notes": "Fund"},
    {"sr": 3, "name": "Shomail Talha",     "phone": "+92 333 3394211", "address": "",                         "amount": 3000,  "notes": "After 2-3 months"},
]

# ─────────────────────────────────────────────
#  CSS  (light + dark mode)
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;600;700&display=swap');

/* ── Light mode tokens ── */
:root {
    --teal:        #0f766e;
    --teal-dark:   #0c4a45;
    --teal-light:  #e4f0ec;
    --muted:       #4f6b66;
    --line:        #cfe0da;
    --bg-card:     #ffffff;
    --bg-hover:    #f7fbfa;
    --text-main:   #10312d;
    --text-td:     #1a1a1a;
    --empty:       #9ab0ab;
    --label-before:#4f6b66;
    --mob-divider: #e4f0ec;
}

/* ── Dark mode tokens ── */
@media (prefers-color-scheme: dark) {
    :root {
        --teal:        #2dd4bf;
        --teal-dark:   #99f6e4;
        --teal-light:  #134e4a;
        --muted:       #94a3b8;
        --line:        #1e3a38;
        --bg-card:     #0f1f1e;
        --bg-hover:    #162e2b;
        --text-main:   #e2f8f4;
        --text-td:     #d1fae5;
        --empty:       #4b6b66;
        --label-before:#7ec8be;
        --mob-divider: #134e4a;
    }
}

html, body, .stApp, label, input, textarea, button {
    font-family: 'Noto Sans', sans-serif !important;
}

footer { visibility: hidden; }
.block-container { padding-top: 1.5rem; max-width: 1200px; }

/* ── login ── */
.login-box { text-align: center; padding: 1rem 0 1.5rem 0; }
.login-box h1 { color: var(--teal-dark); font-size: 1.8rem; margin: .4rem 0 .1rem 0; }
.login-box p  { color: var(--muted);     font-size: .93rem; margin: 0; }

/* ── page header ── */
.pg-header { border-left: 4px solid var(--teal); padding-left: .8rem; margin-bottom: 1rem; }
.pg-header h2 { margin: 0; color: var(--teal-dark); font-size: 1.5rem; }
.pg-header p  { margin: 0; color: var(--muted);     font-size: .88rem; }

/* ── table wrapper ── */
.bm-wrap {
    background: var(--bg-card);
    border: 1px solid var(--line);
    border-radius: 10px;
    overflow-x: auto;
    margin-top: .6rem;
}

/* ── table ── */
.bm-table { width: 100%; border-collapse: collapse; font-size: .9rem; color: var(--text-td); }

.bm-table thead th {
    background:    var(--teal-light);
    color:         var(--teal-dark);
    padding:       .65rem .8rem;
    text-align:    left;
    font-weight:   600;
    border-bottom: 2px solid var(--teal);
    white-space:   nowrap;
}

.bm-table td {
    padding:       .6rem .8rem;
    border-bottom: 1px solid var(--line);
    vertical-align: middle;
    color:         var(--text-td);
}

.bm-table tbody tr:last-child td { border-bottom: 0; }
.bm-table tbody tr:hover          { background: var(--bg-hover); }

.bm-num   { text-align: right; font-variant-numeric: tabular-nums; font-weight: 600; color: var(--text-td); }
.bm-sr    { color: var(--muted); width: 3rem; }
.bm-ph    { white-space: nowrap; font-family: monospace; color: var(--text-td); }
.bm-empty { color: var(--empty); }

/* ── call / whatsapp buttons ── */
.bm-btn {
    display:         inline-flex;
    align-items:     center;
    gap:             .25rem;
    padding:         .3rem .7rem;
    border-radius:   999px;
    font-size:       .8rem;
    font-weight:     600;
    text-decoration: none !important;
    white-space:     nowrap;
    border:          1px solid transparent;
}
.bm-call { color: var(--teal-dark) !important; background: var(--teal-light); border-color: var(--line); }
.bm-wa   { color: #ffffff          !important; background: #0e7a43; }
.bm-btn:hover { filter: brightness(.88); }

/* ── total bar ── */
.bm-total {
    display:         flex;
    justify-content: space-between;
    align-items:     center;
    margin-top:      .7rem;
    padding:         .75rem 1rem;
    background:      var(--bg-card);
    border:          1px solid var(--line);
    border-top:      4px double var(--teal);
    border-radius:   10px;
}
.bm-total-label { color: var(--muted);     font-size: .88rem; }
.bm-total-value { color: var(--teal-dark); font-size: 1.25rem; font-weight: 700; }

/* ── sidebar brand ── */
.bm-brand       { font-size: 1.05rem; font-weight: 700; color: var(--teal-dark); line-height: 1.3; }
.bm-brand small { display: block; font-weight: 400; font-size: .78rem; color: var(--muted); }

/* ── mobile: stack rows as cards ── */
@media (max-width: 700px) {
    .bm-table thead { display: none; }
    .bm-table, .bm-table tbody, .bm-table tr { display: block; width: 100%; }
    .bm-table tr { padding: .4rem 0; border-bottom: 6px solid var(--mob-divider); }
    .bm-table tbody tr:last-child { border-bottom: 0; }
    .bm-table td {
        display:         flex;
        justify-content: space-between;
        gap:             .5rem;
        border:          0;
        padding:         .28rem .8rem;
        text-align:      right;
    }
    .bm-table td::before {
        content:    attr(data-label);
        font-weight: 600;
        color:       var(--label-before);
        text-align:  left;
        flex:        0 0 5.5rem;
        font-size:   .82rem;
    }
    .bm-table td.bm-act          { justify-content: center; }
    .bm-table td.bm-act::before  { display: none; }
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def clean_phone(raw: str) -> str:
    """Strip spaces, dashes, brackets, dots. Keep leading +."""
    text = str(raw or "").strip()
    return ("+" if text.startswith("+") else "") + re.sub(r"\D", "", text)

def wa_digits(phone: str) -> str:
    """Convert to WhatsApp-ready digits (international, no +)."""
    cleaned = clean_phone(phone)
    digits = cleaned.lstrip("+")
    if cleaned.startswith("+"):
        return digits
    if digits.startswith("00"):
        return digits[2:]
    if digits.startswith("0"):            # local Pakistani 0XXX → 92XXX
        return "92" + digits[1:]
    return digits

def fmt_amount(v) -> str:
    try:
        n = float(v)
    except (TypeError, ValueError):
        return "—"
    if n == 0:
        return "—"
    return f"Rs {n:,.0f}" if n == int(n) else f"Rs {n:,.2f}"

def render_table(data: list, search: str) -> None:
    q = search.strip().casefold()
    filtered = [
        r for r in data
        if not q
        or q in r["name"].casefold()
        or q in re.sub(r"\D", "", r["phone"])
        or q in r["phone"]
    ]

    if not filtered:
        st.info("No records match your search.")
        return

    rows_html = ""
    for r in filtered:
        ph   = clean_phone(r["phone"])
        wa   = wa_digits(r["phone"])
        call = f'<a class="bm-btn bm-call" href="tel:{ph}" target="_self">📞 Call</a>'
        chat = f'<a class="bm-btn bm-wa"   href="https://wa.me/{wa}" target="_blank" rel="noopener noreferrer">💬 WhatsApp</a>'
        addr = r.get("address") or ""
        note = r.get("notes")  or ""
        amt  = fmt_amount(r.get("amount", 0))

        rows_html += f"""
        <tr>
          <td data-label="Sr."     class="bm-sr">{r['sr']}</td>
          <td data-label="Name">{r['name']}</td>
          <td data-label="Phone"   class="bm-ph">{ph}</td>
          <td data-label="Address">{'<span class="bm-empty">—</span>' if not addr else addr}</td>
          <td data-label="Amount"  class="bm-num">{amt}</td>
          <td data-label="Notes">{'<span class="bm-empty">—</span>' if not note else note}</td>
          <td class="bm-act">{call}</td>
          <td class="bm-act">{chat}</td>
        </tr>"""

    html = f"""
    <div class="bm-wrap">
      <table class="bm-table">
        <thead>
          <tr>
            <th>Sr.</th><th>Name</th><th>Phone</th><th>Address</th>
            <th class="bm-num">Amount</th><th>Notes</th><th>Call</th><th>WhatsApp</th>
          </tr>
        </thead>
        <tbody>{rows_html}</tbody>
      </table>
    </div>"""
    st.markdown(html, unsafe_allow_html=True)

    total = sum(float(r.get("amount", 0) or 0) for r in filtered)
    st.markdown(
        f'<div class="bm-total">'
        f'<span class="bm-total-label">Total ({len(filtered)} records)</span>'
        f'<span class="bm-total-value">{fmt_amount(total)}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────
#  LOGIN
# ─────────────────────────────────────────────
def show_login():
    st.markdown(
        "<style>[data-testid='stSidebar'],[data-testid='stSidebarCollapsedControl']"
        "{display:none}</style>",
        unsafe_allow_html=True,
    )
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown(
            '<div class="login-box"><div style="font-size:2.2rem">🕌</div>'
            '<h1>Shadman Town<br>Bait ul Maal</h1>'
            '<p>Sign in to view the muawineen lists.</p></div>',
            unsafe_allow_html=True,
        )
        with st.container(border=True):
            with st.form("login"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                if st.form_submit_button("Sign in", type="primary", use_container_width=True):
                    if username.strip() == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                        st.session_state["logged_in"] = True
                        st.rerun()
                    else:
                        st.error("Incorrect username or password.")


# ─────────────────────────────────────────────
#  MAIN APP
# ─────────────────────────────────────────────
def main():
    if not st.session_state.get("logged_in"):
        show_login()
        return

    with st.sidebar:
        st.markdown(
            '<div class="bm-brand">🕌 Shadman Town<br>Bait ul Maal'
            '<small>Muawineen lists</small></div>',
            unsafe_allow_html=True,
        )
        st.divider()
        page = st.radio(
            "Navigate",
            ["🤲  Anat Muawineen", "💰  Fund Muawineen"],
            label_visibility="collapsed",
        )
        st.divider()
        if st.button("Sign out", icon=":material/logout:", use_container_width=True):
            st.session_state.clear()
            st.rerun()

    if "Anat" in page:
        st.markdown(
            '<div class="pg-header"><h2>🤲 Anat Muawineen</h2>'
            '<p>People receiving anat (assistance) from Bait ul Maal.</p></div>',
            unsafe_allow_html=True,
        )
        search = st.text_input("🔍 Search by name or phone", key="anat_q")
        render_table(ANAT_MUAWINEEN, search)

    else:
        st.markdown(
            '<div class="pg-header"><h2>💰 Fund Muawineen</h2>'
            '<p>People contributing to the Bait ul Maal fund.</p></div>',
            unsafe_allow_html=True,
        )
        search = st.text_input("🔍 Search by name or phone", key="fund_q")
        render_table(FUND_MUAWINEEN, search)


main()
