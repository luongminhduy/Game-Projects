

class SceneManager:
    def __init__(self) -> None:
        self.sceneList = {}
        self.currentScene = None
        self.nextScene = None

    def addScene(self, scenes = []):
        for scene in scenes:
            self.sceneList[scene.key] = scene

    def setCurrentScene(self, key):
        self.currentScene = self.sceneList[key]
        
    def getCurrentScene(self):
        return self.currentScene

    def startScene(self, key):
        self.nextScene = self.sceneList[key]

    def update(self):
        if self.nextScene:
            self.currentScene.exit()
            self.currentScene = self.nextScene
            self.nextScene = None

    def printSceneList(self):
        print(self.sceneList)