# Telegram-Downloader
Python script that allows to download video files from a given Telegram group. 

To create the environment you jsut need use conda or miniconda with python `3.6.6` and install the requirements present in the `requirements.txt` file.

**IMPORTANT**: Before executing the script, you need to modify the variables `API_ID` and `API_HASH` inside the code that you have previously created through the following link https://my.telegram.org/apps.

Finally, with the conda environment active, you can execute the following line (replacing the values inside <> with your desired values) to donwload the videos from a given Telegram group.

```python
python telegram_downloader.py -dir "<directory_path>" -gid <group_id> -lim <number_of_files>
```