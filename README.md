# flowlauncher-quick-emacs

Shitty personal plugins to shove text into Emacs from Flow Launcher. Don't use this.

| Keyword | Plugin | What it does |
|---------|--------|-------------|
| `j` | **Quick Journal** | Appends text to today's Log |
| `t` | **Quick Task** | Inserts a TODO in today's Tasks |

Just calls `emacsclientw --eval`. That's it.

## Install

```powershell
cd "$env:APPDATA\FlowLauncher\Plugins"
Copy-Item -Recurse "path\to\repo\journal" "QuickJournal-1.0.0"
Copy-Item -Recurse "path\to\repo\task" "QuickTask-1.0.0"
```

Restart Flow Launcher.

## Usage

```
j buy milk       → appends to Log
t fix auth bug   → inserts TODO in Tasks
```

## Emacs setup

You need these in your Emacs config:

```elisp
(defun my/flowlauncher-insert-journal-entry (text)
  (let ((ts (format-time-string "- [%Y-%m-%d %a %H:%M] ")))
    (require 'org-datetree)
    (find-file "~/journal.org")
    (org-datetree-find-date-create (calendar-current-date))
    (end-of-line) (newline) (insert ts text) (save-buffer)))

(defun my/flowlauncher-insert-journal-task (text)
  (require 'org-datetree)
  (find-file "~/journal.org")
  (org-datetree-find-date-create (calendar-current-date))
  (end-of-line)
  (insert (concat "\n***** TODO " text))
  (save-buffer))
```

## Structure

```
├── journal/     → Quick Journal (keyword j)
├── task/        → Quick Task (keyword t)
├── LICENSE
└── README.md
```
