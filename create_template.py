import pandas as pd

def create_product_template():
    columns = [
        'Name',                    # Required
        'Category',                # Required
        'Description',             # Optional
        'Stock',                   # Required
        'Is Available',            # Optional (Default: True)
        'Is Featured',             # Optional (Default: False)
        'Is Published',            # Optional (Default: True)
        # Camera Specifications
        'Max Resolution',
        'Sensor',
        'Day Night',
        'Shutter',
        'Adjustment Angle',
        'S/N',
        'WDR',
        # Lens Specifications
        'Focal Length',
        'Iris Type',
        'Iris',
        # Video Specifications
        'Video Compression',
        'Frame Rate',
        'Video Bit Rate',
        'Video Stream',
        # Audio Specifications
        'Audio Compression',
        'Two Way Audio',
        'Suppression',
        'Sampling Rate',
        # Storage
        'Edge Storage',
        'Network Storage',
        # Network
        'Protocols',
        'Compatible Integration',
        # General Specifications
        'Power',
        'Dimensions',
        'Weight',
        'Material',
        # Image Paths
        'Photo Main',
        'Photo 1',
        'Photo 2',
        'Photo 3',
        'Photo 4'
    ]

    # Create sample data row
    sample_data = {
        'Name': 'Sample Camera',
        'Category': 'CCTV',
        'Description': 'High-quality surveillance camera',
        'Stock': 10,
        'Is Available': True,
        'Is Featured': False,
        'Is Published': True,
        'Max Resolution': '4K (3840x2160)',
        'Photo Main': 'cameras/sample_main.jpg',
        'Photo 1': 'cameras/sample_1.jpg'
        # Other fields will be empty
    }

    # Create DataFrame with columns and one sample row
    df = pd.DataFrame(columns=columns)
    df.loc[0] = pd.Series(sample_data)

    # Save to Excel
    with pd.ExcelWriter('product_import_template.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Products')
        
        # Get workbook and worksheet objects
        workbook = writer.book
        worksheet = writer.sheets['Products']
        
        # Add formats
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#D9EAD3',
            'border': 1
        })
        
        required_format = workbook.add_format({
            'bold': True,
            'bg_color': '#F4CCCC',
            'border': 1
        })

        # Format headers
        for col_num, value in enumerate(columns):
            if value in ['Name', 'Category', 'Stock']:
                worksheet.write(0, col_num, value + ' *', required_format)
            else:
                worksheet.write(0, col_num, value, header_format)

        # Set column widths
        worksheet.set_column(0, len(columns)-1, 15)
        worksheet.set_column(2, 2, 30)  # Description column wider

    return 'product_import_template.xlsx'

if __name__ == "__main__":
    template_file = create_product_template()
    print(f"Template created: {template_file}")
