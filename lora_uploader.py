import gradio as gr
import os
import shutil

UPLOAD_DIR = "models/Lora"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)
    print(f"[DEBUG] Created upload directory: {UPLOAD_DIR}")
else:
    print(f"[DEBUG] Upload directory already exists: {UPLOAD_DIR}")

def handle_file_upload(file_path):
    try:
        print(f"[DEBUG] Handling file upload: {file_path}")
        
        if file_path is None:
            print("[ERROR] No file path provided.")
            return "No file selected for upload."

        file_name = os.path.basename(file_path)
        destination_path = os.path.join(UPLOAD_DIR, file_name)
        
        # Copy file to target directory
        shutil.copy(file_path, destination_path)
        print(f"[DEBUG] File uploaded successfully to {destination_path}")
        
        return f"File uploaded successfully to {destination_path}"
    except Exception as e:
        print(f"[ERROR] File upload failed: {e}")
        return f"File upload failed: {e}"

def create_ui():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            upload_button = gr.File(label="Upload a file", type="filepath")
            status_box = gr.Textbox(label="Upload Status", value="No file uploaded.", interactive=False)
            
            # Function to handle upload with status updates
            def upload_with_feedback(file_path):
                status_box.update("Uploading...")  # Set status to "Uploading..."
                result = handle_file_upload(file_path)
                status_box.update(result)  # Update status with the result
                return result

            # Trigger upload_with_feedback on file change
            upload_button.change(fn=upload_with_feedback, inputs=upload_button, outputs=status_box)
            print("[DEBUG] File upload handler with feedback linked to button.")
            
    return ui_component

def on_ui_tabs():
    print("[DEBUG] Loading Lora Uploader tab...")
    return [(create_ui(), "LORA upload", "file_uploader_tab")]

try:
    from modules import script_callbacks
    script_callbacks.on_ui_tabs(on_ui_tabs)
    print("[DEBUG] Lora Uploader tab registered successfully.")
except ImportError as e:
    print(f"[ERROR] Failed to import script_callbacks module: {e}")
