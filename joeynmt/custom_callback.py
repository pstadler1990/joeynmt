def custom_callback_epoch(is_best: bool, ckpt_data_path: str) -> None:
    """
    Callback after each successful iteration
    is_best: determines, if this iteration was the best so far
    ckpt_data_path: path to the checkpoint data on the file system
    """
    print('** custom_callback_epoch fired', is_best, ckpt_data_path)
    # TODO:


def custom_callback_train_end(start_time: int, end_time: int) -> None:
    """
    Callback after the training has stopped
    start_time: time of start 
    end_time: time of end
    """
    print('** custom_callback_train_end fired', start_time, end_time)
    # TODO: 

