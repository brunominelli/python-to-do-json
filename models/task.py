import json
class Task():
    def __init__(self, title='', description=''):
        self.title = title
        self.description = description

    def __str__(self):
        return f'''title: {self.title} | description: {self.description}'''

    def create(self, task:dict=None):
        task = task or {}
        if 'title' in task and 'description' in task:
            try:
                with open('data/tasks.json', 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    tasks = data if isinstance(data, list) else []
            except:
                tasks = []
            
            if task.get('title') == '' or task.get('description') == '':
                print('All fields required')
                return
            
            new_task = Task(title=task.get('title'), description=task.get('description'))
            tasks.append(new_task.__dict__)

            with open('data/tasks.json', 'w', encoding='utf-8') as file:
                json.dump(tasks, file, indent=2)
            print(f'Task {self.title} has been created')
        else:
            print('All fields required')

    def read(self):
        with open('data/tasks.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            if data == []:
                print('No tasks registered')
                return
            
            for index, item in enumerate(data):
                task = Task(title=item.get('title'), description=item.get('description'))
                print(f'{index}. {task}')
    
    def read_by_id(self, id):
        with open('data/tasks.json', 'r') as file:
            data = json.load(file) or []
            if data == []:
                print('No tasks registered')
                return
            
            if 0 <= id < len(data):
                task = Task(title=data[id].get('title'), description=data[id].get('description'))
                return task
            else:
                print('Task not found')
                return
    
    def update(self, id, task:dict = None):
        updated_task = self.read_by_id(id=id)
        if updated_task is None:
            return
        
        if 'title' in task and 'description' in task:
            updated_task.title = task.get('title')
            updated_task.description = task.get('description')

            with open('data/tasks.json', 'r', encoding='utf-8') as file:
                data:list = json.load(file)
            
            if 0 <= id < len(data):
                data[id] = updated_task.__dict__
            
            with open('data/tasks.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2)
            
            print(f'Task {id} has been updated: {updated_task}')
        else:
            print('All field required')
                
    def delete(self, id):
        task = self.read_by_id(id=id)
        if task is None:
            print('Task not found')
            return
        
        with open('data/tasks.json', 'r') as file:
            data:list = json.load(file)
            data.remove(data[id])
        
        with open('data/tasks.json', 'w') as file:
            json.dump(data, file, indent=2)
            print(f'Task {id} has been deleted')
