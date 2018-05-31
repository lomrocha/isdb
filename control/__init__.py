from flask \
  import Flask

app = Flask(__name__)

import control.tv_show_control
import control.director_control
import control.cast_control
import control.episode_control
import control.tv_show_cast_episode_control

app.run()
