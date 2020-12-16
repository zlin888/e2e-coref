export BERT_MODEL_PATH="bert_cased_L-12_H-768_A-12"
python extract_bert_features.py --input_file=./ --output_file=./bert_features.hdf5.backup --bert_config_file $BERT_MODEL_PATH/bert_config.json --init_checkpoint $BERT_MODEL_PATH/bert_model.ckpt --vocab_file  $BERT_MODEL_PATH/vocab.txt --do_lower_case=False --stride 1 --window_size 129
