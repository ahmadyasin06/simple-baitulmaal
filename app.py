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
#  CSS  (light + dark mode) — GREEN THEME
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700;800&display=swap');

/* ── Light mode tokens ── */
:root {
    --green:         #16a34a;
    --green-dark:    #14532d;
    --green-mid:     #15803d;
    --green-light:   #dcfce7;
    --green-lighter: #f0fdf4;
    --green-glow:    rgba(22, 163, 74, 0.25);
    --muted:         #4b6b57;
    --line:          #bbf7d0;
    --bg-card:       #ffffff;
    --bg-hover:      #f0fdf4;
    --text-main:     #052e16;
    --text-td:       #1a2e22;
    --empty:         #86b89e;
    --label-before:  #4b6b57;
    --mob-divider:   #dcfce7;
    --shadow:        0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
    --shadow-lg:     0 10px 30px rgba(22, 163, 74, 0.10), 0 4px 10px rgba(0,0,0,0.05);
}

/* ── Dark mode tokens ── */
@media (prefers-color-scheme: dark) {
    :root {
        --green:         #4ade80;
        --green-dark:    #bbf7d0;
        --green-mid:     #22c55e;
        --green-light:   #052e16;
        --green-lighter: #0a1f12;
        --green-glow:    rgba(74, 222, 128, 0.2);
        --muted:         #86b89e;
        --line:          #14532d;
        --bg-card:       #0a1a10;
        --bg-hover:      #0f2a18;
        --text-main:     #dcfce7;
        --text-td:       #c6f6d5;
        --empty:         #4b6b57;
        --label-before:  #6ee7a0;
        --mob-divider:   #14532d;
        --shadow:        0 1px 3px rgba(0,0,0,0.3), 0 1px 2px rgba(0,0,0,0.2);
        --shadow-lg:     0 10px 30px rgba(0,0,0,0.35), 0 4px 10px rgba(0,0,0,0.2);
    }
}

html, body, .stApp, label, input, textarea, button {
    font-family: 'Noto Sans', sans-serif !important;
}

footer { visibility: hidden; }
.block-container { padding-top: 1rem; max-width: 1200px; }

/* ═══════════════════════════════════════════
   LOGIN
   ═══════════════════════════════════════════ */
.login-box { text-align: center; padding: 1.5rem 0 1.5rem 0; }
.login-box .icon {
    font-size: 3rem;
    display: inline-block;
    background: linear-gradient(135deg, var(--green-light), var(--bg-card));
    border-radius: 50%;
    width: 5rem;
    height: 5rem;
    line-height: 5rem;
    border: 2px solid var(--line);
    box-shadow: var(--shadow-lg);
    margin-bottom: .6rem;
}
.login-box h1 {
    background: linear-gradient(135deg, var(--green-dark), var(--green));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 1.9rem;
    font-weight: 800;
    margin: .3rem 0 .2rem 0;
    line-height: 1.2;
}
.login-box p  { color: var(--muted); font-size: .93rem; margin: 0; }

/* ═══════════════════════════════════════════
   NAVBAR (top)
   ═══════════════════════════════════════════ */
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: linear-gradient(135deg, var(--green-dark) 0%, var(--green-mid) 100%);
    border-radius: 14px;
    padding: .65rem .9rem;
    margin-bottom: 1rem;
    box-shadow: var(--shadow-lg);
    flex-wrap: wrap;
    gap: .6rem;
}
.navbar-brand {
    display: flex;
    align-items: center;
    gap: .55rem;
    color: #ffffff;
    font-weight: 700;
    font-size: 1.05rem;
    line-height: 1.2;
}
.navbar-brand .logo {
    font-size: 1.6rem;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.25));
}
.navbar-brand small {
    display: block;
    font-weight: 400;
    font-size: .72rem;
    opacity: .85;
}

/* nav buttons row */
.nav-actions {
    display: flex;
    align-items: center;
    gap: .45rem;
    flex-wrap: wrap;
}

/* ── Page header ── */
.pg-header {
    border-left: 5px solid var(--green);
    padding-left: .9rem;
    margin-bottom: 1rem;
    position: relative;
}
.pg-header h2 {
    margin: 0;
    color: var(--green-dark);
    font-size: 1.55rem;
    font-weight: 800;
    letter-spacing: -.01em;
}
.pg-header p  { margin: .15rem 0 0 0; color: var(--muted); font-size: .88rem; }

/* ═══════════════════════════════════════════
   TABLE
   ═══════════════════════════════════════════ */
.bm-wrap {
    background: var(--bg-card);
    border: 1px solid var(--line);
    border-radius: 14px;
    overflow-x: auto;
    margin-top: .6rem;
    box-shadow: var(--shadow-lg);
}

.bm-table { width: 100%; border-collapse: collapse; font-size: .9rem; color: var(--text-td); }

.bm-table thead th {
    background: linear-gradient(135deg, var(--green-dark), var(--green-mid));
    color: #ffffff;
    padding: .75rem .85rem;
    text-align: left;
    font-weight: 700;
    font-size: .82rem;
    text-transform: uppercase;
    letter-spacing: .04em;
    white-space: nowrap;
    position: sticky;
    top: 0;
    z-index: 1;
}
.bm-table thead th:first-child { border-top-left-radius: 13px; }
.bm-table thead th:last-child  { border-top-right-radius: 13px; }

.bm-table td {
    padding: .65rem .85rem;
    border-bottom: 1px solid var(--line);
    vertical-align: middle;
    color: var(--text-td);
}

.bm-table tbody tr:last-child td { border-bottom: 0; }
.bm-table tbody tr { transition: background .15s ease; }
.bm-table tbody tr:hover          { background: var(--bg-hover); }

/* ── number / amount styling ── */
.bm-num {
    text-align: right;
    font-variant-numeric: tabular-nums;
    font-weight: 700;
    color: var(--green-dark);
    font-size: .92rem;
    white-space: nowrap;
}

/* amount badge */
.bm-amt-badge {
    display: inline-block;
    background: var(--green-light);
    color: var(--green-dark);
    padding: .22rem .6rem;
    border-radius: 999px;
    font-weight: 700;
    font-size: .84rem;
    border: 1px solid var(--line);
    white-space: nowrap;
}
.bm-amt-zero {
    display: inline-block;
    color: var(--empty);
    font-weight: 600;
    font-size: .84rem;
}

.bm-sr    { color: var(--muted); width: 3rem; font-weight: 600; }
.bm-ph    { white-space: nowrap; font-family: 'Noto Sans', monospace; color: var(--text-td); font-weight: 500; }
.bm-empty { color: var(--empty); }

/* ── call / whatsapp buttons ── */
.bm-btn {
    display:         inline-flex;
    align-items:     center;
    gap:             .25rem;
    padding:         .35rem .75rem;
    border-radius:   999px;
    font-size:       .78rem;
    font-weight:     700;
    text-decoration: none !important;
    white-space:     nowrap;
    border:          1px solid transparent;
    transition:      all .15s ease;
    box-shadow:      var(--shadow);
}
.bm-call {
    color: var(--green-dark) !important;
    background: var(--green-light);
    border-color: var(--line);
}
.bm-call:hover { background: var(--green); color: #fff !important; border-color: var(--green); }
.bm-wa {
    color: #ffffff !important;
    background: linear-gradient(135deg, #16a34a, #15803d);
    border-color: #15803d;
}
.bm-wa:hover { filter: brightness(1.1); box-shadow: 0 4px 12px var(--green-glow); }

/* ═══════════════════════════════════════════
   TOTAL BAR
   ═══════════════════════════════════════════ */
.bm-total {
    display:         flex;
    justify-content: space-between;
    align-items:     center;
    margin-top:      .8rem;
    padding:         .85rem 1.1rem;
    background:      linear-gradient(135deg, var(--green-lighter), var(--bg-card));
    border:          1px solid var(--line);
    border-top:      5px double var(--green);
    border-radius:   14px;
    box-shadow:      var(--shadow-lg);
    flex-wrap:       wrap;
    gap:             .5rem;
}
.bm-total-label { color: var(--muted);     font-size: .9rem;  font-weight: 600; }
.bm-total-value {
    color: var(--green-dark);
    font-size: 1.3rem;
    font-weight: 800;
    letter-spacing: -.01em;
}

/* ═══════════════════════════════════════════
   SIDEBAR BRAND
   ═══════════════════════════════════════════ */
.bm-brand       { font-size: 1.05rem; font-weight: 800; color: var(--green-dark); line-height: 1.3; }
.bm-brand small { display: block; font-weight: 400; font-size: .78rem; color: var(--muted); }

/* ═══════════════════════════════════════════
   SEARCH INPUT POLISH
   ═══════════════════════════════════════════ */
.stTextInput input {
    border-radius: 10px !important;
    border: 1.5px solid var(--line) !important;
    transition: border-color .2s ease, box-shadow .2s ease;
}
.stTextInput input:focus {
    border-color: var(--green) !important;
    box-shadow: 0 0 0 3px var(--green-glow) !important;
}

/* ═══════════════════════════════════════════
   MOBILE: stack rows as cards
   ═══════════════════════════════════════════ */
@media (max-width: 700px) {
    .navbar { border-radius: 12px; padding: .55rem .7rem; }
    .navbar-brand { font-size: .95rem; }
    .navbar-brand .logo { font-size: 1.4rem; }
    .nav-actions { width: 100%; justify-content: stretch; }
    .nav-actions > * { flex: 1; }

    .bm-table thead { display: none; }
    .bm-table, .bm-table tbody, .bm-table tr { display: block; width: 100%; }
    .bm-table tr {
        padding: .5rem 0;
        border-bottom: 6px solid var(--mob-divider);
        border-radius: 10px;
        margin-bottom: .3rem;
    }
    .bm-table tbody tr:last-child { border-bottom: 0; }
    .bm-table td {
        display:         flex;
        justify-content: space-between;
        gap:             .5rem;
        border:          0;
        padding:         .3rem .85rem;
        text-align:      right;
    }
    .bm-table td::before {
        content:      attr(data-label);
        font-weight:  700;
        color:        var(--label-before);
        text-align:   left;
        flex:         0 0 5.5rem;
        font-size:    .82rem;
    }
    .bm-table td.bm-act          { justify-content: center; gap: .5rem; }
    .bm-table td.bm-act::before  { display: none; }
    .bm-num { text-align: right; }
    .bm-amt-badge, .bm-amt-zero { font-size: .8rem; }
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

def amount_badge(v) -> str:
    """Return styled HTML badge for amount."""
    try:
        n = float(v)
    except (TypeError, ValueError):
        return '<span class="bm-amt-zero">—</span>'
    if n == 0:
        return '<span class="bm-amt-zero">—</span>'
    text = f"Rs {n:,.0f}" if n == int(n) else f"Rs {n:,.2f}"
    return f'<span class="bm-amt-badge">{text}</span>'

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
        amt  = amount_badge(r.get("amount", 0))

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
        f'<span class="bm-total-label">📊 Total ({len(filtered)} records)</span>'
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
            '<div class="login-box">'
            '<div class="icon">🕌</div>'
            '<h1>Shadman Town<br>Bait ul Maal</h1>'
            '<p>Sign in to view the muawineen lists.</p></div>',
            unsafe_allow_html=True,
        )
        with st.container(border=True):
            with st.form("login"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                if st.form_submit_button("🔐 Sign in", type="primary", use_container_width=True):
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

    # ── initialise page state ──
    if "page" not in st.session_state:
        st.session_state["page"] = "anat"

    # ── TOP NAVBAR ──
    st.markdown(
        """
        <div class="navbar">
          <div class="navbar-brand">
            <span class="logo">🕌</span>
            <span>Shadman Town Bait ul Maal
              <small>Muawineen Management</small>
            </span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── nav buttons row (green themed) ──
    nav1, nav2, nav3 = st.columns([1, 1, 4])
    with nav1:
        if st.button(
            "🤲  Anat Muawineen",
            use_container_width=True,
            type="primary" if st.session_state["page"] == "anat" else "secondary",
        ):
            st.session_state["page"] = "anat"
            st.rerun()
    with nav2:
        if st.button(
            "💰  Fund Muawineen",
            use_container_width=True,
            type="primary" if st.session_state["page"] == "fund" else "secondary",
        ):
            st.session_state["page"] = "fund"
            st.rerun()
    with nav3:
        _, signout_col = st.columns([4, 1])
        with signout_col:
            if st.button("🚪 Sign out", use_container_width=True):
                st.session_state.clear()
                st.rerun()

    st.divider()

    # ── page content ──
    if st.session_state["page"] == "anat":
        st.markdown(
            '<div class="pg-header"><h2>🤲 Anat Muawineen</h2>'
            '<p>People receiving anat (assistance) from Bait ul Maal.</p></div>',
            unsafe_allow_html=True,
        )
        search = st.text_input("🔍 Search by name or phone", key="anat_q", placeholder="Type a name or phone number…")
        render_table(ANAT_MUAWINEEN, search)

    else:
        st.markdown(
            '<div class="pg-header"><h2>💰 Fund Muawineen</h2>'
            '<p>People contributing to the Bait ul Maal fund.</p></div>',
            unsafe_allow_html=True,
        )
        search = st.text_input("🔍 Search by name or phone", key="fund_q", placeholder="Type a name or phone number…")
        render_table(FUND_MUAWINEEN, search)


main()
