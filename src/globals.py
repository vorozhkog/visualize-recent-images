import os

import supervisely as sly
from dotenv import load_dotenv


if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api.from_env()
SLY_APP_DATA_DIR = sly.app.get_data_dir()


selected_team = sly.env.team_id()
selected_workspace = sly.env.workspace_id()
selected_project = sly.env.project_id(raise_not_found=False)
selected_dataset = sly.env.dataset_id(raise_not_found=False)

delay = int(os.environ.get("modal.state.UpdateDelay", 2))
col_num = int(os.environ.get("modal.state.GridWidth", 2))

# project_info = api.project.get_info_by_id(selected_project) if selected_project else None

# last_time = project_info.updated_at
# current_time = None
