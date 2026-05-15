import streamlit as st
from pathlib import Path
import os
import shutil

st.set_page_config(page_title="CRUD File Manager", page_icon="📁")

st.title("📁 CRUD File & Folder Manager")


# =========================
# Show Files and Folders
# =========================
def show_files():
    st.subheader("📂 Current Files & Folders")

    p = Path('.')
    items = list(p.rglob('*'))

    if items:
        for index, file in enumerate(items):
            st.write(f"{index + 1}. {file}")
    else:
        st.info("No files or folders found.")


show_files()

st.divider()

# =========================
# Sidebar Menu
# =========================
option = st.sidebar.selectbox(
    "Choose Operation",
    (
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    )
)

# =========================
# Create File
# =========================
if option == "Create File":

    st.header("📝 Create File")

    file_name = st.text_input("Enter file name")
    content = st.text_area("Enter file content")

    if st.button("Create File"):

        p = Path(file_name)

        if p.exists():
            st.error("FILE ALREADY EXISTS")

        else:
            with open(file_name, 'w') as file:
                file.write(content)

            st.success("FILE CREATED SUCCESSFULLY")


# =========================
# Read File
# =========================
elif option == "Read File":

    st.header("📖 Read File")

    file_name = st.text_input("Enter file name")

    if st.button("Read File"):

        p = Path(file_name)

        if p.exists():

            with open(file_name, 'r') as file:
                data = file.read()

            st.text_area("File Content", data, height=300)

        else:
            st.error("FILE NOT FOUND")


# =========================
# Update File
# =========================
elif option == "Update File":

    st.header("✏️ Update File")

    file_name = st.text_input("Enter file name")

    update_type = st.radio(
        "Choose Update Type",
        ("Overwrite", "Append")
    )

    content = st.text_area("Enter new content")

    if st.button("Update File"):

        p = Path(file_name)

        if p.exists():

            if update_type == "Overwrite":

                with open(file_name, 'w') as file:
                    file.write(content)

                st.success("FILE OVERWRITTEN")

            else:

                with open(file_name, 'a') as file:
                    file.write(content)

                st.success("CONTENT APPENDED")

        else:
            st.error("FILE NOT FOUND")


# =========================
# Delete File
# =========================
elif option == "Delete File":

    st.header("🗑️ Delete File")

    file_name = st.text_input("Enter file name")

    if st.button("Delete File"):

        p = Path(file_name)

        if p.exists():

            os.remove(p)
            st.success("FILE DELETED")

        else:
            st.error("FILE NOT FOUND")


# =========================
# Rename File
# =========================
elif option == "Rename File":

    st.header("🔄 Rename File")

    old_name = st.text_input("Enter current file name")
    new_name = st.text_input("Enter new file name")

    if st.button("Rename File"):

        p = Path(old_name)

        if p.exists():

            p.rename(new_name)
            st.success("FILE RENAMED")

        else:
            st.error("FILE NOT FOUND")


# =========================
# Create Folder
# =========================
elif option == "Create Folder":

    st.header("📂 Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):

        p = Path(folder_name)

        if p.exists():
            st.error("FOLDER ALREADY EXISTS")

        else:
            p.mkdir()
            st.success("FOLDER CREATED")


# =========================
# Delete Folder
# =========================
elif option == "Delete Folder":

    st.header("❌ Delete Folder")

    folder_name = st.text_input("Enter folder name")

    delete_type = st.radio(
        "Delete Option",
        ("Empty Folder Only", "Delete Folder With Files")
    )

    if st.button("Delete Folder"):

        p = Path(folder_name)

        if p.exists():

            try:

                if delete_type == "Empty Folder Only":
                    p.rmdir()

                else:
                    shutil.rmtree(p)

                st.success("FOLDER DELETED")

            except Exception as e:
                st.error(f"ERROR: {e}")

        else:
            st.error("FOLDER NOT FOUND")