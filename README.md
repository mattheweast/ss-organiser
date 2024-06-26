# Screenshot organiser

#### Organise your screenshots - By Matt East

<p>As an apprentice, I am forever taking screenshot after screenshot as proof of work, for my portfolio. At the end of each day/week I would either forget to organise them or just loose track of them completely.</p>
<p>I created this tool so that at the end of each day at the click of a button you can organise your screenshots into dated folders and also set a name for the current project/ticket you are working on.</p>

### Feature List:
<ul>
    <li>Organise screenshots into a folder off the desktop.</li>
    <li>Automatically create sub folders with the date screenshots were taken.</li>
    <li>Config file added to set project/ticket name to combine with the date taken.</li>
    <li>Notification to inform you how many screenshots have been organised.</li>
</ul>

### Feature Roadmap:

# Setup 

#### Setup file paths

```python
def organise_screenshots():
    desktop_folder = os.path.join(os.path.expanduser('~'), 'Desktop')
    screenshot_folder = os.path.join(os.path.expanduser('~'), 'Documents', 'apple_apprenticeship', 'screenshots')
```

<p>The <b>desktop_folder</b> variable is there to set the location of where your screenshots land when taken.</p>
<p>The <b>screenshots_folder</b> variable is the location of where you want your screenshots to be stored. You will need to create the destination <b>screenshot folder</b> in which future folders will be generated.</p>

# How it works

<p>As an apprentice software engineer it is important to have a full understanding of the code. This is my attempt at an explanation of this. I am always open to feedback especially when it comes to refactoring. So feel free branch and send me a MR with anything that may help (I am not looking for full feature updates though as this is a personal educational project for myself <3).</p>