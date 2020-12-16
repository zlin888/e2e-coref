export BERT_MODEL_PATH="albert_base"
python extract_albert_features.py --input_file=./ --output_file=./albert_features.hdf5 --bert_config_file $BERT_MODEL_PATH/albert_config.json --init_checkpoint $BERT_MODEL_PATH/model.ckpt-best --vocab_file  $BERT_MODEL_PATH/30k-clean.model --do_lower_case=False --stride 1 --window_size 129
