# Cloning This Repository (Git LFS Required)

If you would like to test the CleaningDataset notebook then follow this. If you don't need the CleaningDataset notebook then ignore this. 
This repository uses Git LFS (Large File Storage) to store large datasets (CSV files).
To clone and use this project correctly, you must install Git LFS before pulling the repo.

### 1. Install Git LFS

##### macOS:

```sh
brew install git-lfs
```
##### Windows:
Download from: https://git-lfs.com/

##### Linux: 
```bash
sudo apt-get install git-lfs
```

#### 2. Initialize Git LFS
Run this once, before cloning or inside the repo
```sh
git lfs install
```

#### 3. Clone the repo
```sh
git clone https://github.com/Abdullah-Mohammed-OTU/Machine_Learning_Project.git
```

#### 4. Verify that LFS files were downloaded
```sh
git lfs ls-files
```

#### Notes
- If you clone without installing Git LFS, the dataset files will appear as small pointer files instead of CSVs.
- Do not manually edit .gitattributes unless you know what you’re doing.


