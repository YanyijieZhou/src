README - create_project.sh
==========================

What this does
---------------

`create_project.sh` is a Bash script that reads a simple YAML file describing a folder structure and creates the corresponding folders under a target root (default: `~/ongoing/projects`).

Usage
-----

Basic (use default config and root):

```bash
~/ongoing/src/my_py/create_project/scripts/create_project.sh
```

Specify a config file and a different root:

```bash
~/ongoing/src/my_py/create_project/scripts/create_project.sh --config /path/to/folder_structure.yaml --root ~/ongoing/my-new-projects
```

Dry-run to preview actions:

```bash
~/ongoing/src/my_py/create_project/scripts/create_project.sh --dry-run
```

Assumptions & limitations
-------------------------

- The parser is intentionally simple and designed for the example YAML you provided (mappings + lists with 2-space indentation). It does not fully implement YAML spec (no anchors, complex types, or folded scalars).
- If your YAML becomes more complex, install `yq` or use a small Python/Ruby script to parse safely.

Location of default config
--------------------------

By default the script looks for the config at `../config/folder_structure.yaml` relative to the `scripts/` folder. In your repository that is:

```bash
src/my_py/create_project/config/folder_structure.yaml
```

If you keep your YAML there you can run the script without passing `--config`.

Examples
--------

Given your example YAML under `config/folder_structure.yaml`, running the script will create (by default) folder trees like:

- ~/ongoing/projects/01_ProjectManagement/01_Meeting
- ~/ongoing/projects/01_ProjectManagement/02_Ideas
- ~/ongoing/projects/02_Data/00_Raw_Data/00_transcipts/00_transcrpits_cn
- ~/ongoing/projects/02_Data/00_Raw_Data/00_transcipts/01_transcripts_en
- ~/ongoing/projects/02_Data/01_Processed
- ~/ongoing/projects/03_Analysis/00_Source
- ~/ongoing/projects/03_Analysis/01_Code
- ~/ongoing/projects/08_Literature
- ~/ongoing/projects/09_Dissemination

Contact
-------

If you want the script to support more YAML features (anchors, alternative indent sizes), tell me which features and I can update it to either use `yq` or a small Python/Ruby parser fallback.
