import logging 

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)       
    
    # create formatter ONCE and reuse it
    fmt = logging.Formatter(              
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"     
    )

    # console handler - INFO and above
    console_handler = logging.StreamHandler()  
    console_handler.setLevel(logging.INFO)     
    console_handler.setFormatter(fmt)          

    # file handler - DEBUG and above
    file_handler = logging.FileHandler("pipeline.log", mode="a")  
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(fmt)

    logger.addHandler(console_handler)   
    logger.addHandler(file_handler)

    return logger                        