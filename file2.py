
# from pathlib import Path
# import os 

# def createfile():
#     try:
#         name=input("plz tell ur file name:- ")
#         path=Path(name)
#         if not path.exists():
#             with open(path,'w') as fs:
#                 data=input("file me kia lkhna chahty ho ")
#                 fs.write(data) 
#             print("file ban gai hy ")
#         else:
#             print("Error file name alredy exsist")
#     except Exception as err:
#         print(f" ea apka err hy {err}")
# def readfile():
#     try:
#         name=input("plz tell ur file name")
#         path=Path(name)
#         if path.exists():
#             with open(path,'r') as fs :
#                 content=fs.read()
#                 print(f"ur file content is \n {content}")
#         else:
#             print("no such file exsists")
#     except Exception as err:
#         print(f"ap ka ree {err}")
# def updatefile():
#     try:
#         name = input("plz tell ur file name ")
#         path = Path(name)
#         if path.exists():
#             print("operations ")
#             print("1 . renameing the file")
#             print("2 . appending the content")
#             print("3 . overwrite the file")

#             choice = int(input("enter ur option: "))
#             if choice == 1:
#                 newname = input("plz tell new name: ")
#                 new_path = Path(newname)
#                 if not new_path.exists():
#                     path.rename(new_path)
#                     print("rename ho gia hy ")
#                 else:
#                     print("file already exsist")
#             elif choice == 2:
#                 with open(path, 'a') as fs:
#                     data = input("file me kia lkhna chahty ho (append): ")
#                     fs.write(data)
#                 print("content appended")
#             elif choice == 3:
#                 with open(path, 'w') as fs:
#                     data = input("file me kia lkhna chahty ho (overwrite): ")
#                     fs.write(data)
#                 print("file overwritten")
#             else:
#                 print("invalid option")
#         else:
#             print("no such file exsists")
#     except Exception as err:
#         print(f"ap ka ree {err}")

# def deletefile():
#     try:
#         name = input("plz tell ur file name ")
#         path = Path(name)
#         if path.exists():
#             path.unlink()
#             print("your file deleted")
#         else:
#             print("no such file exsists")
#     except Exception as err:
#         print(f"ap ka ree {err}")


# print("for creating file please press 1")
# print("for reading file please press 2")
# print("for updating file please press 3")
# print("for deleting file please press 4")

# nmbr=int(input("what you want to do:-"))

# if nmbr==1:
#     createfile()
# if nmbr==2:
#     readfile()
    
# if nmbr==3:
#     updatefile()
# if nmbr==4:
#     deletefile()
import streamlit as st
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Smart File Hub",
    page_icon="📂",
    layout="centered"
)

# --- APP BRANDING ---
st.title("📂 Smart File Management Hub")
st.markdown("A lightweight, elegant, and secure dashboard for local file operations.")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Navigation")
operation = st.sidebar.radio(
    "Choose an Action:",
    ["✨ Create File", "📄 Read File", "🔄 Update File", "🗑️ Delete File"]
)

st.sidebar.divider()
st.sidebar.markdown("💡 *Built with Python and Streamlit*")

# --- OPERATION 1: CREATE FILE ---
if operation == "✨ Create File":
    st.subheader("Create a New File")
    
    with st.form("create_form", clear_on_submit=True):
        file_name = st.text_input("Enter File Name (e.g., notes.txt):").strip()
        content = st.text_area("Write File Content:", placeholder="Type your text here...")
        submitted = st.form_submit_button("Create File")
        
        if submitted:
            if not file_name:
                st.warning("⚠️ Please provide a valid file name.")
            else:
                file_path = Path(file_name)
                if not file_path.exists():
                    try:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(content)
                        st.success(f"🎉 Success! '{file_name}' created successfully.")
                    except Exception as error:
                        st.error(f"❌ Error creating file: {error}")
                else:
                    st.error("❌ Error: A file with this name already exists.")

# --- OPERATION 2: READ FILE ---
elif operation == "📄 Read File":
    st.subheader("Read File Content")
    
    file_name = st.text_input("Enter File Name to Read:").strip()
    if st.button("Read File", type="primary"):
        if not file_name:
            st.warning("⚠️ Please enter a file name.")
        else:
            file_path = Path(file_name)
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    st.info(f"📋 **Content of '{file_name}':**")
                    st.text_area("File Output:", value=content, height=200, disabled=True)
                except Exception as error:
                    st.error(f"❌ Error reading file: {error}")
            else:
                st.error("❌ Error: No such file exists.")

# --- OPERATION 3: UPDATE FILE ---
elif operation == "🔄 Update File":
    st.subheader("Modify an Existing File")
    
    file_name = st.text_input("Enter File Name to Update:").strip()
    if file_name:
        file_path = Path(file_name)
        if file_path.exists():
            
            # Sub-options inside tabs for cleaner UI
            tab1, tab2, tab3 = st.tabs(["✏️ Rename", "➕ Append Content", "📝 Overwrite"])
            
            with tab1:
                new_name = st.text_input("Enter New File Name:").strip()
                if st.button("Apply Rename"):
                    if new_name:
                        new_path = Path(new_name)
                        if not new_path.exists():
                            try:
                                file_path.rename(new_path)
                                st.success(f"💪 Renamed successfully to '{new_name}'!")
                            except Exception as error:
                                st.error(f"❌ Failed to rename: {error}")
                        else:
                            st.error("❌ Error: A file with that name already exists.")
                    else:
                        st.warning("⚠️ Enter a valid new name.")
                        
            with tab2:
                append_content = st.text_area("Content to Append:", key="append_box")
                if st.button("Append Text"):
                    try:
                        with open(file_path, 'a', encoding='utf-8') as file:
                            file.write(append_content)
                        st.success("➕ Content appended successfully!")
                    except Exception as error:
                        st.error(f"❌ Error appending: {error}")
                        
            with tab3:
                overwrite_content = st.text_area("New Content (Overwrites old data):", key="overwrite_box")
                if st.button("Overwrite File", type="destructive"):
                    try:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(overwrite_content)
                        st.success("📝 File overwritten successfully!")
                    except Exception as error:
                        st.error(f"❌ Error overwriting: {error}")
        else:
            st.error("❌ Error: No such file exists.")

# --- OPERATION 4: DELETE FILE ---
elif operation == "🗑️ Delete File":
    st.subheader("Delete a File")
    
    file_name = st.text_input("Enter File Name to Delete:").strip()
    if file_name:
        file_path = Path(file_name)
        if file_path.exists():
            st.warning(f"⚠️ Warning: Are you sure you want to permanently delete '{file_name}'?")
            
            if st.button("Confirm Delete", type="destructive"):
                try:
                    file_path.unlink()
                    st.success(f"🗑️ '{file_name}' has been deleted successfully.")
                except Exception as error:
                    st.error(f"❌ Error deleting file: {error}")
        else:
            st.error("❌ Error: No such file exists.")
