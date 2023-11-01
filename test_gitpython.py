import git

repo = git.Repo(search_parent_directories=True)
# desc = repo.git.describe('--tags')
# closesttag = repo.git.describe('--tags','--abbrev=0')
dirty = repo.is_dirty()
# distance = desc.split(sep='-')[-2]
# print(desc)
print(repo.is_dirty())
print(repo.tags)
print(repo.git.rev_list('--tags','--max-count=1'))
# print(closesttag)

# print(f'{closesttag}.{distance}.local')
