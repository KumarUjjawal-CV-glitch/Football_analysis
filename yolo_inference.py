from ultralytics import YOLO


model = YOLO('models/football_player_model_best.pt')

results = model.predict('input_videos/in_videos.mp4',save=True)
print(results[0])
print('=====================================================')
for box in results[0].boxes:
    print(box)