#[tauri::command]
fn health() -> &'static str {
    "ok"
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![health])
        .run(tauri::generate_context!())
        .expect("failed to run TraderAI desktop shell");
}
