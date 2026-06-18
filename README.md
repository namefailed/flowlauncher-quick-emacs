# Flow Launcher Quick Emacs

Two independent Flow Launcher plugins for Emacs capture:

| Plugin | Keyword | Action |
|--------|---------|--------|
| **Quick Journal** | `j` | Append text to today's **Log** section |
| **Quick Task** | `t` | Insert a `***** TODO` heading in today's **Tasks** section |

Each plugin is fully self-contained — copy its directory to
`%APPDATA%\FlowLauncher\Plugins\` and restart Flow Launcher.

## Prerequisites

- [Flow Launcher](https://flowlauncher.com/)
- [Emacs](https://www.gnu.org/software/emacs/) with a running daemon (`emacs --daemon`)
- `emacsclientw` on `PATH`
- Elisp functions in your Emacs config (see [Emacs Setup](#emacs-setup))

## Installation

```powershell
cd "$env:APPDATA\FlowLauncher\Plugins"

# Quick Journal
Copy-Item -Recurse "path\to\repo\journal" "QuickJournal-1.0.0"

# Quick Task
Copy-Item -Recurse "path\to\repo\task" "QuickTask-1.0.0"
```

Restart Flow Launcher.

## Usage

```
j buy milk          → appends to today's Log
t fix auth bug      → inserts a TODO in today's Tasks
```

## Emacs Setup

The plugins call `my/flowlauncher-insert-transcript` and
`my/flowlauncher-insert-task`. Define them in your Emacs config:

```elisp
(defun my/flowlauncher-insert-transcript (text)
  (require 'org-datetree)
  (find-file "~/journal.org")
  (org-datetree-find-date-create (calendar-current-date))
  (end-of-line)
  (insert (concat "\n- [" (format-time-string "%Y-%m-%d %a %H:%M") "] " text))
  (save-buffer))

(defun my/flowlauncher-insert-task (text)
  (require 'org-datetree)
  (find-file "~/journal.org")
  (org-datetree-find-date-create (calendar-current-date))
  (end-of-line)
  (insert (concat "\n***** TODO " text))
  (save-buffer))
```

## File structure

```
flowlauncher-quick-emacs/
├── journal/
│   ├── plugin.json
│   ├── run.py
│   └── Images/
│       └── journal.png
├── task/
│   ├── plugin.json
│   ├── run.py
│   └── Images/
│       └── task.png
├── LICENSE
└── README.md
```

## License

MIT
