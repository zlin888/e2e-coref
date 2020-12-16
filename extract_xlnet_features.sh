export BERT_MODEL_PATH="xlnet_cased_L-12_H-768_A-12"
python extract_xlnet_features.py --input_file=./ --output_file=./xlnet_features.hdf5 --bert_config_file $BERT_MODEL_PATH/xlnet_config.json --init_checkpoint $BERT_MODEL_PATH/xlnet_model.ckpt --vocab_file  $BERT_MODEL_PATH/spiece.model --do_lower_case=False --stride 1 --window_size 129
