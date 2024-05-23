import os

def get_directory_structure(root_dir):
    structure = []
    total_size = 0
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        level = dirpath.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        
        # Calculate directory size
        dir_size = sum(os.path.getsize(os.path.join(dirpath, f)) for f in filenames)
        total_size += dir_size
        
        structure.append('{}{}/ ({} files, {} bytes)'.format(indent, os.path.basename(dirpath), len(filenames), dir_size))
        
        subindent = ' ' * 4 * (level + 1)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            structure.append('{}{} ({} bytes)'.format(subindent, filename, file_size))
    
    structure.append('Total project size: {} bytes'.format(total_size))
    return structure

def write_structure_to_file(structure, output_file):
    with open(output_file, 'w') as f:
        for line in structure:
            f.write(line + '\n')
