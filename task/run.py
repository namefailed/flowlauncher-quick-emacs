import subprocess
from flowlauncher import FlowLauncher, FlowLauncherAPI


class QuickTask(FlowLauncher):

    def query(self, query):
        query = query.strip()
        if not query:
            return [{
                "Title": "Quick Task",
                "SubTitle": "t <text> — add a TODO task",
                "IcoPath": "Images\\task.png",
                "JsonRPCAction": {"method": "noop", "parameters": []}
            }]
        preview = query[:120] + ("..." if len(query) > 120 else "")
        return [{
            "Title": f"Task: {preview}",
            "SubTitle": "Add TODO to today's Tasks",
            "IcoPath": "Images\\task.png",
            "JsonRPCAction": {
                "method": "capture",
                "parameters": [query]
            }
        }]

    def capture(self, text):
        escaped = text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
        try:
            subprocess.run(
                ["emacsclientw", "-a", "emacs", "--eval",
                 f'(my/phoneme-insert-task "{escaped}")'],
                capture_output=True,
                timeout=10,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        except FileNotFoundError:
            FlowLauncherAPI.show_msg("Quick Task Error", "emacsclientw not found")
            return
        except subprocess.TimeoutExpired:
            FlowLauncherAPI.show_msg("Quick Task Error", "Emacs did not respond within 10s")
            return
        except Exception as e:
            FlowLauncherAPI.show_msg("Quick Task Error", str(e))
            return
        FlowLauncherAPI.close_app()

    def noop(self):
        pass


if __name__ == "__main__":
    QuickTask()
