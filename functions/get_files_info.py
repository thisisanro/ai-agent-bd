import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)

        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_full_path):
            return f'Error: "{directory}" is not a directory'

        entries = os.listdir(abs_full_path)
        lines = []

        for entry in entries:
            try:
                entry_path = os.path.join(abs_full_path, entry)
                is_dir = os.path.isdir(entry_path)
                size = os.path.getsize(entry_path)
                lines.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")
            except Exception as e:
                lines.append(f"- {entry}: Error reading info ({str(e)})")

        return "\n".join(lines)

    except Exception as e:
        return f"Error: {str(e)}"

