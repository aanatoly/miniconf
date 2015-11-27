# chaining git-hooks
Here you can find collection of usefull git hooks and a script
to chain them. 

With it, you can have many pre-commit scripts without explcitly writing 
a wrapper to call them one by one.

## Usage 
1. Copy `hook-chain` script to the `.git/hooks` directory
```
cd my-project/.git/hooks
git clone https://github.com/aanatoly/miniconf.git /tmp/miniconf
cp /tmp/miniconf/git-hooks/hook-chain .
```
2. Copy relevant hooks and name them TYPE-NO-NAME. For example, to have 2
   pre-commit hooks, do this:
```
cp /tmp/miniconf/git-hooks/pre-commit-[0-9]*  .
```

3. create link, named as commit pointing to `hook-chain`
```
rm pre-commit
ln -sf hook-chain pre-commit
```
That is it.
