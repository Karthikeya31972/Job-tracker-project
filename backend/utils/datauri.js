import path from 'path';

const getDataUri = (file) => {
    if (!file) {
        throw new Error('No file provided');
    }
    
    const dataUri = `data:${file.mimetype};base64,${file.buffer.toString('base64')}`;
    
    return {
        content: dataUri
    };
};

export default getDataUri;
