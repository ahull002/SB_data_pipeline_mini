{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "excellent-clark",
   "metadata": {},
   "outputs": [],
   "source": [
    "# to represent the project's package\n",
    "import pandas as pd\n",
    "from pathlib import Path\n",
    "\n",
    "\n",
    "def get_my_data() -> pd.DataFrame:\n",
    "    module_path: Path = Path(__file__)\n",
    "    file_path: Path = (module_path / \"../../data/data.csv\").resolve()\n",
    "    return pd.read_csv(file_path)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
