# postgres
- brew services start postgresql@15
- brew services stop postgresql@15
- netstat -an | grep 5432

# redis
```sh
   brew services start redis
   brew services info redis
   redis-server
   brew services stop redis
```
# celery
celery -A core worker --loglevel=INFO

# git 
git fetch

git log origin/main

git merge origin/main

# show local branch
git branch

# show local + remote branch
git branch -a

# show remote branch
git branch -r

git branch -vv

git remote show origin


If your branch is one commit ahead of the main branch and you want to merge it into the main branch, you can follow these steps:

1. **Ensure You Are on the Main Branch:**
   ```bash
   git checkout main
   ```

2. **Pull the Latest Changes from the Remote Main Branch:**
   ```bash
   git pull origin main
   ```
   This step ensures that you have the latest changes from the remote main branch.

3. **Merge Your Branch into the Main Branch:**
   ```bash
   git merge <your-branch-name>
   ```
   Replace `<your-branch-name>` with the name of your branch.

   If there are no conflicts, Git will automatically perform the merge. If there are conflicts, Git will pause and allow you to resolve them. After resolving conflicts, you can continue the merge with:
   ```bash
   git merge --continue
   ```

4. **Resolve any Conflicts (if needed):**
   If there are conflicts, Git will pause the merge, and you need to resolve conflicts manually. Open the conflicted files, resolve the conflicts, and then continue with the merge.

5. **Commit the Merge:**
   After resolving conflicts (if any), commit the merge changes:
   ```bash
   git commit -m "Merge branch 'your-branch-name' into main"
   ```

6. **Push Changes to the Remote Repository:**
   ```bash
   git push origin main
   ```
   This command pushes the merged changes to the remote main branch.

Now, your changes from your branch are merged into the main branch, and both your local and remote main branches are up to date.




To make the `main` branch the default branch (`HEAD`) on the remote repository (`origin`), you'll need to perform the following steps:

1. **Locally Update Default Branch:**
   Change the default branch locally to `main`:
   ```bash
   git branch -m main
   ```

2. **Push Changes to Remote Repository:**
   Push the local changes to the remote repository, and set `main` as the default branch on the remote repository:
   ```bash
   git push -u origin main
   ```

3. **Update Remote Repository's HEAD:**
   Update the remote repository's `HEAD` to point to the `main` branch:
   ```bash
   git remote set-head origin -a
   ```

   This command will set the default branch on the remote repository to the currently checked-out branch locally (which is `main` after renaming).

4. **Verify Changes:**
   Verify that the remote repository's default branch has been updated:
   ```bash
   git remote show origin
   ```

   Look for the line that says "HEAD branch" and ensure it indicates `main`.

After completing these steps, the default branch on the remote repository (`origin`) should be set to `main`. Note that this operation affects the remote repository, so make sure you have the necessary permissions to perform these changes.