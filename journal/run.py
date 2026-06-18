import subprocess
from flowlauncher import FlowLauncher, FlowLauncherAPI


class QuickJournal(FlowLauncher):

    def query(self, query):
        query = query.strip()
        if not query:
            return [{
                "Title": "Quick Journal",
                "SubTitle": "j <text> — append to today's Log",
                "IcoPath": "Images\\journal.png",
                "JsonRPCAction": {"method": "noop", "parameters": []}
            }]
        preview = query[:120] + ("..." if len(query) > 120 else "")
        return [{
            "Title": f"Journal: {preview}",
            "SubTitle": "Append to today's Log",
            "IcoPath": "Images\\journal.png",
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
                 f'(my/flowlauncher-insert-transcript "{escaped}")'],
                capture_output=True,
                timeout=10,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        except FileNotFoundError:
            FlowLauncherAPI.show_msg("Quick Journal Error", "emacsclientw not found")
            return
        except subprocess.TimeoutExpired:
            FlowLauncherAPI.show_msg("Quick Journal Error", "Emacs did not respond within 10s")
            return
        except Exception as e:
            FlowLauncherAPI.show_msg("Quick Journal Error", str(e))
            return
        FlowLauncherAPI.close_app()

    def noop(self):
        pass


if __name__ == "__main__":
    QuickJournal()
