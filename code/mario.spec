# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'F:/code/Mario-Level/resources/fonts', 'resources/fonts' ),
         ( 'F:/code/Mario-Level/resources/graphics', 'resources/graphics' ),
         ( 'F:/code/Mario-Level/resources/music', 'resources/music' ),
		 ( 'F:/code/Mario-Level/resources/sound', 'resources/sound' ),
         ]
a = Analysis(['mario_level_1.py'],
             pathex=['F:\\code\\Mario-Level'],
             binaries=[],
             datas = added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='mario_level_1',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='mario_level_1')
