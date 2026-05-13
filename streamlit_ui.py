"""
File Manager — Streamlit UI
Run with:  streamlit run file_manager_streamlit.py
"""

import streamlit as st
from pathlib import Path
import os


# ─────────────────────────────────────────────
#  Core logic (unchanged from original)
# ─────────────────────────────────────────────

def get_all_items():
    p = Path('')
    return list(p.rglob('*'))


def create_file(file_name: str, content: str):
    p = Path(file_name)
    if p.exists():
        return False, "⚠️ FILE ALREADY EXISTS"
    with open(file_name, 'w') as f:
        f.write(content)
    return True, "✅ FILE CREATED SUCCESSFULLY"


def read_file(file_name: str):
    p = Path(file_name)
    if p.exists():
        with open(file_name, 'r') as f:
            return True, f.read()
    return False, "❌ FILE NOT FOUND"


def update_file(file_name: str, content: str, mode: str = 'w'):
    p = Path(file_name)
    if not p.exists():
        return False, "❌ FILE DOES NOT EXIST"
    with open(file_name, mode) as f:
        f.write(content)
    return True, "✅ FILE UPDATED SUCCESSFULLY"


def delete_file(file_name: str):
    p = Path(file_name)
    if p.exists():
        os.remove(p)
        return True, "✅ FILE DELETED"
    return False, "❌ FILE DOES NOT EXIST"


def rename_file(file_name: str, new_name: str):
    p = Path(file_name)
    if p.exists():
        p.rename(new_name)
        return True, "✅ FILE RENAMED SUCCESSFULLY"
    return False, "❌ FILE NOT FOUND"


def create_folder(folder_name: str):
    p = Path(folder_name)
    if p.exists():
        return False, "⚠️ FOLDER ALREADY EXISTS"
    p.mkdir()
    return True, "✅ FOLDER CREATED"


def delete_folder(folder_name: str):
    p = Path(folder_name)
    if p.exists():
        p.rmdir()
        return True, "✅ FOLDER DELETED"
    return False, "❌ FOLDER DOES NOT EXIST"


# ─────────────────────────────────────────────
#  Page config
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="File Manager",
    page_icon="⚡",
    layout="wide",
)

# ─────────────────────────────────────────────
#  Custom CSS
# ─────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'JetBrains Mono', monospace;
}

/* Dark background */
.stApp { background: #0f0f1a; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: #1a1a2e;
    border-right: 1px solid #2e2e4a;
}

/* Card-like containers */
.fm-card {
    background: #1e1e35;
    border: 1px solid #3a3a5c;
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1rem;
}

/* Section heading */
.fm-heading {
    color: #c084fc;
    font-weight: 700;
    font-size: 0.85rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}

/* Hero banner */
.fm-hero {
    background: linear-gradient(135deg, #1e1e35 0%, #2a1a4a 100%);
    border: 1px solid #7c6af7;
    border-radius: 12px;
    padding: 1.4rem 2rem;
    margin-bottom: 1.6rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}
.fm-hero h1 {
    color: #7c6af7;
    font-size: 1.8rem;
    font-weight: 700;
    margin: 0;
    letter-spacing: 0.05em;
}
.fm-hero p { color: #94a3b8; margin: 0; font-size: 0.78rem; }

/* Override button */
.stButton > button {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 600 !important;
    border-radius: 6px !important;
    border: none !important;
    transition: transform 0.1s, box-shadow 0.1s !important;
}
.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 14px rgba(124, 106, 247, 0.35) !important;
}

/* Inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    font-family: 'JetBrains Mono', monospace !important;
    background: #12121f !important;
    color: #e2e8f0 !important;
    border: 1px solid #3a3a5c !important;
    border-radius: 6px !important;
}

/* Success / Error / Warning boxes */
.stSuccess, .stError, .stWarning, .stInfo {
    font-family: 'JetBrains Mono', monospace !important;
    border-radius: 8px !important;
}

/* Explorer tree */
.explorer-item {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    color: #94a3b8;
    padding: 2px 0;
}
.explorer-folder { color: #fb923c; }
.explorer-file   { color: #60a5fa; }

/* Tab override */
[data-baseweb="tab"] {
    font-family: 'JetBrains Mono', monospace !important;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  Sidebar — Explorer
# ─────────────────────────────────────────────

with st.sidebar:
    st.markdown("### 📂 Explorer")
    if st.button("🔄 Refresh", use_container_width=True):
        st.rerun()

    items = get_all_items()
    dirs  = sorted([i for i in items if i.is_dir()])
    files = sorted([i for i in items if i.is_file()])

    st.markdown(f"<small style='color:#94a3b8'>{len(dirs)} folders · {len(files)} files</small>",
                unsafe_allow_html=True)
    st.markdown("---")

    if dirs:
        st.markdown("<p style='color:#fb923c;font-size:0.75rem;font-weight:700;'>FOLDERS</p>",
                    unsafe_allow_html=True)
        for d in dirs:
            st.markdown(f"<div class='explorer-item explorer-folder'>📁 {d}</div>",
                        unsafe_allow_html=True)
    if files:
        st.markdown("<p style='color:#60a5fa;font-size:0.75rem;font-weight:700;margin-top:0.6rem'>FILES</p>",
                    unsafe_allow_html=True)
        for f in files:
            st.markdown(f"<div class='explorer-item explorer-file'>📄 {f}</div>",
                        unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  Main area
# ─────────────────────────────────────────────

st.markdown("""
<div class="fm-hero">
  <div>
    <h1>⚡ File Manager</h1>
    <p>Create · Read · Update · Delete · Rename files and folders</p>
  </div>
</div>
""", unsafe_allow_html=True)

tab_files, tab_folders = st.tabs(["📄  Files", "📁  Folders"])


# ══════════════════════════════════════════════
#  FILES TAB
# ══════════════════════════════════════════════

with tab_files:

    col1, col2 = st.columns([1, 1], gap="large")

    # ── Create ──────────────────────────────
    with col1:
        st.markdown('<p class="fm-heading">✨ Create File</p>', unsafe_allow_html=True)
        with st.container(border=True):
            cf_name    = st.text_input("File name", placeholder="e.g. notes.txt", key="cf_name")
            cf_content = st.text_area("Content", placeholder="Enter file content…", height=120, key="cf_content")
            if st.button("➕  Create File", type="primary", use_container_width=True):
                if cf_name.strip():
                    ok, msg = create_file(cf_name.strip(), cf_content)
                    st.success(msg) if ok else st.error(msg)
                    if ok: st.rerun()
                else:
                    st.warning("⚠️ Please enter a file name.")

    # ── Read ────────────────────────────────
    with col2:
        st.markdown('<p class="fm-heading">📖 Read File</p>', unsafe_allow_html=True)
        with st.container(border=True):
            rf_name = st.text_input("File name", placeholder="e.g. notes.txt", key="rf_name")
            if st.button("📖  Read File", use_container_width=True):
                if rf_name.strip():
                    ok, data = read_file(rf_name.strip())
                    if ok:
                        st.success(f"Contents of **{rf_name}**")
                        st.code(data, language="text")
                    else:
                        st.error(data)
                else:
                    st.warning("⚠️ Please enter a file name.")

    st.divider()

    col3, col4, col5 = st.columns(3, gap="medium")

    # ── Update ──────────────────────────────
    with col3:
        st.markdown('<p class="fm-heading">💾 Update File</p>', unsafe_allow_html=True)
        with st.container(border=True):
            uf_name    = st.text_input("File name", key="uf_name", placeholder="e.g. notes.txt")
            uf_content = st.text_area("New content", height=100, key="uf_content")
            uf_mode    = st.radio("Write mode", ["Overwrite", "Append"],
                                  horizontal=True, key="uf_mode")
            if st.button("💾  Update", use_container_width=True):
                if uf_name.strip():
                    mode = 'w' if uf_mode == "Overwrite" else 'a'
                    ok, msg = update_file(uf_name.strip(), uf_content, mode)
                    st.success(msg) if ok else st.error(msg)
                else:
                    st.warning("⚠️ Please enter a file name.")

    # ── Delete ──────────────────────────────
    with col4:
        st.markdown('<p class="fm-heading">🗑 Delete File</p>', unsafe_allow_html=True)
        with st.container(border=True):
            df_name = st.text_input("File name", key="df_name", placeholder="e.g. notes.txt")
            confirm = st.checkbox("I confirm I want to delete this file", key="df_confirm")
            if st.button("🗑  Delete File", type="primary", use_container_width=True,
                         disabled=not confirm):
                if df_name.strip():
                    ok, msg = delete_file(df_name.strip())
                    st.success(msg) if ok else st.error(msg)
                    if ok: st.rerun()
                else:
                    st.warning("⚠️ Please enter a file name.")

    # ── Rename ──────────────────────────────
    with col5:
        st.markdown('<p class="fm-heading">✏️ Rename File</p>', unsafe_allow_html=True)
        with st.container(border=True):
            rn_old = st.text_input("Current name", key="rn_old", placeholder="old_name.txt")
            rn_new = st.text_input("New name",     key="rn_new", placeholder="new_name.txt")
            if st.button("✏️  Rename", use_container_width=True):
                if rn_old.strip() and rn_new.strip():
                    ok, msg = rename_file(rn_old.strip(), rn_new.strip())
                    st.success(msg) if ok else st.error(msg)
                    if ok: st.rerun()
                else:
                    st.warning("⚠️ Please fill both name fields.")


# ══════════════════════════════════════════════
#  FOLDERS TAB
# ══════════════════════════════════════════════

with tab_folders:

    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        st.markdown('<p class="fm-heading">📁 Create Folder</p>', unsafe_allow_html=True)
        with st.container(border=True):
            mk_name = st.text_input("Folder name", key="mk_name", placeholder="e.g. my_folder")
            if st.button("➕  Create Folder", type="primary", use_container_width=True):
                if mk_name.strip():
                    ok, msg = create_folder(mk_name.strip())
                    st.success(msg) if ok else st.error(msg)
                    if ok: st.rerun()
                else:
                    st.warning("⚠️ Please enter a folder name.")

    with col_b:
        st.markdown('<p class="fm-heading">🗑 Delete Folder</p>', unsafe_allow_html=True)
        with st.container(border=True):
            rm_name = st.text_input("Folder name", key="rm_name",
                                    placeholder="e.g. my_folder (must be empty)")
            rm_confirm = st.checkbox("I confirm I want to delete this folder", key="rm_confirm")
            if st.button("🗑  Delete Folder", type="primary", use_container_width=True,
                         disabled=not rm_confirm):
                if rm_name.strip():
                    ok, msg = delete_folder(rm_name.strip())
                    st.success(msg) if ok else st.error(msg)
                    if ok: st.rerun()
                else:
                    st.warning("⚠️ Please enter a folder name.")

    st.info("ℹ️ Folders must be **empty** before they can be deleted (Python's `rmdir` restriction).")