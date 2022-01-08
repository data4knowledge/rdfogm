# GitHub

## Personal Access Token

- Login in to github on the web
- Top right hand menu, choose **Settings**
- Scroll down to **Developer settings**
- Select **Personal access tokens**
- Generate the token and copy and keep somewhere safe

Then

- Run the Mac Keychain Access utility (found in ```Applications\Utility``` directory)
- Search for github.com, double-click
- Choose Show Password
- You will need to enter your macbook password, and enter
- You will be able to see the password now and just paste the token you already generated, and save the changes.

That should be it

If not see this https://gist.github.com/nepsilon/0fd0c779f76d7172f12477ba9d71bb66

## Ignore

To add a folder/directory to ```.gitignore```, include their paths and put a / at the end:

```
<folder_name>/
```

Note: .gitignore ignores untracked files. Files already tracked by Git are not affected. To stop tracking a file that is currently tracked, use ```git rm -r --cached <folder_name>```

For .DS_Store files see this post
https://stackoverflow.com/questions/107701/how-can-i-remove-ds-store-files-from-a-git-repository
